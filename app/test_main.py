from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_over_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 1.06
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_over_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 0.94
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing_same_rate() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 1
        assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_at_plus_5_percent_boundary() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_at_minus_5_percent_boundary() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"
