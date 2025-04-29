from app.main import cryptocurrency_action

from unittest.mock import patch, Mock


# Сильне зростання: prediction / current_rate > 1.05
@patch("app.main.random.random", return_value=0.2)
@patch("app.main.random.choice", return_value="increase")
def test_buy_more(mock_choice: Mock, mock_random: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"
    mock_choice.assert_called_once()
    mock_random.assert_called_once()


# Сильне падіння: prediction / current_rate < 0.95
@patch("app.main.random.random", return_value=0.9)
@patch("app.main.random.choice", return_value="decrease")
def test_sell_all(mock_choice: Mock, mock_random: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"
    mock_choice.assert_called_once()
    mock_random.assert_called_once()


# Невелика зміна курсу: між -5% і +5%
@patch("app.main.random.random", return_value=0.98)
@patch("app.main.random.choice", return_value="decrease")
def test_rate_95_percent_do_nothing(mock_choice: Mock,
                                    mock_random: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
    mock_choice.assert_called_once()
    mock_random.assert_called_once()


@patch("app.main.random.random", return_value=1.05)
@patch("app.main.random.choice", return_value="increase")
def test_rate_105_percent_do_nothing(mock_choice: Mock,
                                     mock_random: Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
    mock_choice.assert_called_once()
    mock_random.assert_called_once()
