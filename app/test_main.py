from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_when_prediction_above_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all_when_prediction_below_minus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_within_range() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=102):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_do_nothing_when_prediction_exactly_plus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_do_nothing_when_prediction_exactly_minus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
