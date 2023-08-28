import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1, 1, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency")

    ]
)
def test_type_of_variables(
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_get_exchange_rate_prediction:
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected
