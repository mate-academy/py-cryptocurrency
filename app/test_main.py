from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_act_do_nothing_decrease(
        mocked_get_exchange_rate_prediction:
        int) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_act_do_nothing_increase(
        mocked_get_exchange_rate_prediction: int
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_act_buy_more_crypt(
        mocked_get_exchange_rate_prediction: int
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.91
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_act_sell_all_crypt(
        mocked_get_exchange_rate_prediction: int
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
