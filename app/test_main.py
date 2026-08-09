import app.main as main
from unittest.mock import patch, MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_buy(mock_pred: MagicMock) -> None:
    current_rate = 100
    mock_pred.return_value = current_rate * 1.06  # +6%
    result = main.cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell(mock_pred: MagicMock) -> None:
    current_rate = 100
    mock_pred.return_value = current_rate / 1.06
    result = main.cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_pred: MagicMock) -> None:
    current_rate = 100
    mock_pred.return_value = 104  # +4% — в межах 5%
    result = main.cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_pred: MagicMock) -> None:
    current_rate = 100
    mock_pred.return_value = 95  # 95/100 = 0.95
    result = main.cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_pred: MagicMock) -> None:
    current_rate = 100
    mock_pred.return_value = 105  # 105/100 = 1.05
    result = main.cryptocurrency_action(current_rate)
    assert result == "Do nothing"
