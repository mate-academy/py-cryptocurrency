from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=110)
def test_buy_more(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=90)
def test_sell_all(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=103)
def test_do_nothing(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_exactly_5_percent_increase(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_exactly_5_percent_decrease(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
