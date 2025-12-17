from app.main import cryptocurrency_action
from unittest.mock import patch


def test_buy_more_cryptocurrency_when_prediction_higher_5_percent() -> None:
    current_rate = 100
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_sell_cryptocurrency_prediction_lower_more_than_5_percent() -> None:
    current_rate = 100
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def do_nothing() -> None:
    current_rate = 100
    with patch("app.main.get_exchange_rate_prediction", return_value=102):
        result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
