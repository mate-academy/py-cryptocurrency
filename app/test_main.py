from unittest.mock import patch

from app.main import cryptocurrency_action


def test_should_suggest_buy_if_current_rate_more_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.4):
        assert cryptocurrency_action(1.3) == "Buy more cryptocurrency"


def test_should_suggest_sell_if_current_rate_less_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.4):
        assert cryptocurrency_action(1.5) == "Sell all your cryptocurrency"


def test_should_suggest_do_nothing_if_current_rate_has_small_diff() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.4):
        assert cryptocurrency_action(1.42) == "Do nothing"


def test_should_suggest_do_nothing_if_current_rate_exactly_5_higher() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.05):
        assert cryptocurrency_action(1.0) == "Do nothing"


def test_should_suggest_do_nothing_if_current_rate_exactly_5_lower() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.95):
        assert cryptocurrency_action(1.0) == "Do nothing"
