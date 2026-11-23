from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=106)
def test_buy_when_rate_grows(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=94)
def test_sell_when_rate_falls(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=103)
def test_do_nothing_when_rate_low_grows(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_do_nothing_when_rate_grow_small(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_do_nothing_when_rate_fall_small(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
