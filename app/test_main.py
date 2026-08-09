from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_more(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_upper_bound(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lower_bound(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
