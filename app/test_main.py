from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    action = cryptocurrency_action(1.0)
    assert action == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94
    action = cryptocurrency_action(1.0)
    assert action == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_buy(
        mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    action = cryptocurrency_action(1.0)
    assert action == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_sell(
        mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    action = cryptocurrency_action(1.0)
    assert action == "Do nothing"
