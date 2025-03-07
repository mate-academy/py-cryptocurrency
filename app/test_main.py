from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_up(get_exchange_rate_prediction: float) -> None:

    get_exchange_rate_prediction.return_value = 1.1
    result = cryptocurrency_action(1)
    print(result)
    assert result == "Buy more cryptocurrency"
    get_exchange_rate_prediction.assert_called_once()
    get_exchange_rate_prediction.assert_called_once_with(1)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_down(get_exchange_rate_prediction: float) -> None:

    get_exchange_rate_prediction.return_value = 1.88
    result = cryptocurrency_action(2)
    print(result)
    assert result == "Sell all your cryptocurrency"
    get_exchange_rate_prediction.assert_called_once()
    get_exchange_rate_prediction.assert_called_once_with(2)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_still(get_exchange_rate_prediction: float) -> None:

    get_exchange_rate_prediction.return_value = 3.00
    result = cryptocurrency_action(3)
    print(result)
    assert result == "Do nothing"
    get_exchange_rate_prediction.assert_called_once()
    get_exchange_rate_prediction.assert_called_once_with(3)
