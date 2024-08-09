from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto(
        mock_get_rate: MagicMock
) -> None:
    mock_get_rate.return_value = 105.01
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_crypto(
        mock_get_rate: MagicMock
) -> None:
    mock_get_rate.return_value = 94.99
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_low(
mock_get_rate: MagicMock
) -> None:
    mock_get_rate.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_high(
mock_get_rate: MagicMock
) -> None:
    mock_get_rate.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"
