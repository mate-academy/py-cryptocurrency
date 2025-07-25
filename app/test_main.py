from unittest.mock import patch
from app.main import cryptocurrency_action

def test_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.06):
        assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"

def test_sell_all_your_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.94):
        assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"

def test_do_nothing_when_difference_is_small() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.04):
        assert cryptocurrency_action(1.0) == "Do nothing"

def test_do_nothing_when_difference_is_small_lower() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.96):
        assert cryptocurrency_action(1.0) == "Do nothing"
