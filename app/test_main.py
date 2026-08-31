
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_buy_more(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_sell_all(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_do_nothing(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_do_nothing_boundary_up(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_do_nothing_boundary_down(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_do_nothing_minus(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
