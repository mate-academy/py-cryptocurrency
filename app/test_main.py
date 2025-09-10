from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=105.1) as mock_pred:
        result = cryptocurrency_action(100.0)
        assert result == "Buy more cryptocurrency"
        mock_pred.assert_called_once_with(100.0)


def test_sell_all() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=94.9) as mock_pred:
        result = cryptocurrency_action(100.0)
        assert result == "Sell all your cryptocurrency"
        mock_pred.assert_called_once_with(100.0)


def test_do_nothing_equal() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=100.0) as mock_pred:
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"
        mock_pred.assert_called_once_with(100.0)


def test_do_nothing_small_increase() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=104.9) as mock_pred:
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"
        mock_pred.assert_called_once_with(100.0)


def test_do_nothing_small_decrease() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=95.1) as mock_pred:
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"
        mock_pred.assert_called_once_with(100.0)


def test_do_nothing_exact_upper_boundary() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=105.0) as mock_pred:
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"
        mock_pred.assert_called_once_with(100.0)


def test_do_nothing_exact_lower_boundary() -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=95.0) as mock_pred:
        result = cryptocurrency_action(100.0)
        assert result == "Do nothing"
        mock_pred.assert_called_once_with(100.0)
