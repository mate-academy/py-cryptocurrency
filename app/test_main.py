from unittest.mock import patch
from app.main import cryptocurrency_action


def test_should_buy_more_when_rate_increase() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_should_sell_all_when_rate_decrease() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_should_do_nothing_when_rate_increase_small() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=104):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_should_do_nothing_when_rate_decrease_small() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=96):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
