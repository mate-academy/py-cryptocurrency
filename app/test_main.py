from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 22
    assert cryptocurrency_action(20) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 10
    assert cryptocurrency_action(20) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
