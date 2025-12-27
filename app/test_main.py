import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_action",
    [
        (45, 90, "Buy more cryptocurrency"),
        (158, 128, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate: int | float,
        expected_action: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_action
