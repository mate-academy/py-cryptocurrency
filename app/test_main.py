from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more(
        moke_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    moke_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all_your_crypto(
        moke_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    moke_get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_prediction_is_95(
        moke_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    moke_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_prediction_is_105(
        moke_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    moke_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
