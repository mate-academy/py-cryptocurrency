from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.1
    result = cryptocurrency_action(1.0)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.8
    result = cryptocurrency_action(1.0)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.98
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_float(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 2.1
    result = cryptocurrency_action(2.0)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_float(mock_get_exchange_rate_prediction: MagicMock) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.7
    result = cryptocurrency_action(2.0)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"
