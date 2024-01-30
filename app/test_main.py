# write your code here
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_is_buy(mock_get_exchange_rate_prediction: callable) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_is_sell(mock_get_exchange_rate_prediction: callable) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_is_do_nothing_when_plus_5(mock_get_exchange_rate_prediction: callable) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_is_do_nothing_when_minus_5(mock_get_exchange_rate_prediction: callable) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"
