from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_crypto(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105.1
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_crypto(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 100.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"
