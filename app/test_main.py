from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 106
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 94
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_plus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 105
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_minus_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 95
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_zero_changes() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 100
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
