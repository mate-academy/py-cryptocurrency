from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=106)
def test_buy(mock_prediction: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=94)
def test_sell(mock_prediction: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=103)
def test_do_nothing_up(mock_prediction: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=97)
def test_do_nothing_down(mock_prediction: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_exactly_plus_5_percent(mock_prediction: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_exactly_minus_5_percent(mock_prediction: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
