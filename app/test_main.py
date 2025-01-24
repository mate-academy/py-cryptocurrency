from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(get_prediction: Union[int, float]) -> None:
    get_prediction.return_value = 100
    assert cryptocurrency_action(94) == "Buy more cryptocurrency"
    assert cryptocurrency_action(107) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(101) == "Do nothing"
    get_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
    get_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
