from unittest.mock import patch
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy_more() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106.0):
        result = cryptocurrency_action(100.0)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94.0):
        result = cryptocurrency_action(100.0)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=102.0):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"


def test_cryptocurrency_action_do_nothing_edge_case_105_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing", ("You should not buy "
                                        "cryptocurrency when prediction_rate "
                                        "/ current_rate == 1.05")


def test_cryptocurrency_action_do_nothing_edge_case_95_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing", ("You should not sell "
                                        "cryptocurrency when prediction_rate "
                                        "/ current_rate == 0.95")
