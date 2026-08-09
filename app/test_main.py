# write your code here
from .main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.mark.parametrize("current_rate,"
                         "prediction_rate, result",
                         [(100, 110, "Buy more cryptocurrency"),
                          (100, 106, "Buy more cryptocurrency"),
                          (100, 90, "Sell all your cryptocurrency"),
                          (100, 94, "Sell all your cryptocurrency"),
                          (100, 105, "Do nothing"),
                          (100, 95, "Do nothing")])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: mock.Mock,
                               current_rate: int,
                               prediction_rate: int,
                               result: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
