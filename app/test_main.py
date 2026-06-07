from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 110
        result = cryptocurrency_action(current_rate=100)
        assert result == "Buy more cryptocurrency"


def test_sell() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 90
        result = cryptocurrency_action(current_rate=100)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 100
        result = cryptocurrency_action(current_rate=100)
        assert result == "Do nothing"


def test_do_nothing_at_95_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 95
        result = cryptocurrency_action(current_rate=100)
        assert result == "Do nothing"


def test_do_nothing_at_105_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 105
        result = cryptocurrency_action(current_rate=100)
        assert result == "Do nothing"
