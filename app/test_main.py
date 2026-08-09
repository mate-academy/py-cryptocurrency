import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate, result",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
    ]
)
def test_cryptocurrency_action(rate_prediction: mock.MagicMock,
                               prediction_rate: float, result: str) -> None:
    rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(1) == result
