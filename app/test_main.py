from unittest.mock import patch
from app.main import cryptocurrency_action


def test_should_buy_when_prediction_more_than_5_percent_higher() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_should_sell_when_prediction_more_than_5_percent_lower() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_do_nothing_when_difference_is() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Do nothing"


def test_should_do_nothing_when_difference_is_less() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Do nothing"
