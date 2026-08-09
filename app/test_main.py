from unittest.mock import patch
from app import main


def test_buy_more_cryptocurrency() -> None:
    """Test when predicted rate is more than 5% higher."""
    with patch.object(
        main, "get_exchange_rate_prediction", return_value=105.1
    ):
        result = main.cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    """Test when predicted rate is more than 5% lower."""
    with patch.object(
        main, "get_exchange_rate_prediction", return_value=94.9
    ):
        result = main.cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_do_nothing_when_difference_small() -> None:
    """Test when rate difference is less than 5%."""
    with patch.object(
        main, "get_exchange_rate_prediction", return_value=102
    ):
        result = main.cryptocurrency_action(100)
        assert result == "Do nothing"


def test_do_nothing_at_lower_boundary() -> None:
    """Test when ratio is exactly 0.95."""
    with patch.object(
        main, "get_exchange_rate_prediction", return_value=95
    ):
        result = main.cryptocurrency_action(100)
        assert result == "Do nothing"


def test_do_nothing_at_upper_boundary() -> None:
    """Test when ratio is exactly 1.05."""
    with patch.object(
        main, "get_exchange_rate_prediction", return_value=105
    ):
        result = main.cryptocurrency_action(100)
        assert result == "Do nothing"
