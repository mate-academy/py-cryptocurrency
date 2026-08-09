from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_high(mock_current_rate: int) -> None:
    mock_current_rate.return_value = 16
    result = cryptocurrency_action(10)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_low(mock_current_rate: int) -> None:
    mock_current_rate.return_value = 9
    result = cryptocurrency_action(10)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_final(mock_current_rate: int) -> None:
    mock_current_rate.return_value = 9.5
    result = cryptocurrency_action(10)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_equal_high_boundary(mock_current_rate: int) -> None:
    mock_current_rate.return_value = 10.5
    result = cryptocurrency_action(10)

    assert result == "Do nothing"
