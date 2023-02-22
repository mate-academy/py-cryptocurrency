from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_buy_action(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"
    mocked_prediction.assert_called_once_with(100)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_sell_action(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 50
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
    mocked_prediction.assert_called_once_with(100)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_do_nothing_action(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_prediction.assert_called_with(100)

    mocked_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_prediction.assert_called_with(100)
