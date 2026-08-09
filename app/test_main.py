from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.06):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.94):
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_rate_105_percent_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.05):
        assert cryptocurrency_action(1) == "Do nothing"


def test_rate_95_percent_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.95):
        assert cryptocurrency_action(1) == "Do nothing"
