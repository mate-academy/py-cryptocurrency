import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
    ]
)
def test_cryptocurrency_action_all_boundary_cases(
        current_rate: int | float,
        predicted_rate: int | float,
        expected: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_exchange_rate:
        mock_exchange_rate.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == expected
