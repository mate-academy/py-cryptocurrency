import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "rate_prediction, current_rate, result",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (1, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (0.94, 1, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_rate_prediction: mock.Mock,
        rate_prediction: int | float,
        current_rate: int | float,
        result: str) -> None:
    mock_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(current_rate) == result
