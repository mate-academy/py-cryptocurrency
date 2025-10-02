import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_coins():
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency():
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


@pytest.mark.parametrize("predicted", [105, 96, 100, 95])  # dentro do limite
def test_do_nothing(predicted):
    with patch("app.main.get_exchange_rate_prediction", return_value=predicted):
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
