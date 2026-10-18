from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy(mock_pred: MagicMock) -> None:
    mock_pred.return_value = 110

    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell(mock_pred: MagicMock) -> None:
    mock_pred.return_value = 0

    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_pred: MagicMock) -> None:
    mock_pred.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_pred: MagicMock) -> None:
    mock_pred.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
