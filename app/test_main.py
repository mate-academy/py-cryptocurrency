from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.06):
        result = cryptocurrency_action(1.0)
    assert result == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.94):
        result = cryptocurrency_action(1.0)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing_high() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=1.05):
        result = cryptocurrency_action(1.0)
    assert result == "Do nothing"


def test_do_nothing_low() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=0.95):
        result = cryptocurrency_action(1.0)
    assert result == "Do nothing"
