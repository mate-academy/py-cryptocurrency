# write your code here
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_buying_cryptocurrency(mocked_prediction: int | float) -> None:
    mocked_prediction.return_value = 14
    assert cryptocurrency_action(7) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mocked_prediction: int | float) -> None:
    mocked_prediction.return_value = 7
    assert cryptocurrency_action(14) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mocked_prediction: int | float) -> None:
    mocked_prediction.return_value = 10.2
    assert cryptocurrency_action(10) == "Do nothing"
