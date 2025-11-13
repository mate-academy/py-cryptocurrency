from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_when_rate_increases_over_five_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_when_rate_drops_over_five_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_when_rate_change_is_small() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=103):
        assert cryptocurrency_action(100) == "Do nothing"

    with patch("app.main.get_exchange_rate_prediction", return_value=97):
        assert cryptocurrency_action(100) == "Do nothing"
