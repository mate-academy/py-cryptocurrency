from unittest import mock

from app.main import cryptocurrency_action


# write your code here

@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_calls_get_exchange_rate_prediction(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 100.10
    cryptocurrency_action(100.10)
    mocked_get_exchange_rate_prediction.assert_called_once_with(100.10)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_tells_to_buy_more(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 110.0
    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_tells_to_stop_buying(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 104.0
    assert cryptocurrency_action(100.0) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 105.0
    assert cryptocurrency_action(100.0) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 95.0
    assert cryptocurrency_action(100.0) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_tells_to_sell(
        mocked_get_exchange_rate_prediction: mock.MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 90.0
    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"
