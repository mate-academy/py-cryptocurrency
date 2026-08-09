import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 101, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    current_rate: int | float,
    predicted_rate: int | float,
    expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == expected_result
