from app.main import cryptocurrency_action
from unittest.mock import patch


def test_buy_more_when_prediction_strictly_more_than_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=5.26):  # > 5.25
        assert cryptocurrency_action(5.00) == "Buy more cryptocurrency"


def test_do_nothing_when_prediction_exactly_plus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=5.25):  # +5%
        assert cryptocurrency_action(5.00) == "Do nothing"


def test_sell_all_when_prediction_strictly_more_than_5_percent_lower() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=4.74):  # < 4.75
        assert cryptocurrency_action(5.00) == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_exactly_minus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=4.75):  # -5%
        assert cryptocurrency_action(5.00) == "Do nothing"


def test_do_nothing_when_prediction_within_5_percent_range() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=5.02):
        assert cryptocurrency_action(5.00) == "Do nothing"
