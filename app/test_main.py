from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_exchange,prediction_rate,result",
    [
        (1, 2, "Buy more cryptocurrency"),
        (1, 0, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction_rate: float,
                               current_exchange: int | float,
                               prediction_rate: int | float,
                               result: str) -> None:
    mocked_prediction_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_exchange) == result
