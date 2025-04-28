from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=1.2)
def test_higher_than_5_percents(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=0.8)
def test_lower_than_5_percents(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=1.02)
def test_0_percents(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_rate_105_percent_do_nothing(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing",\
        ("You should not buy cryptocurrency when prediction_rate "
         "/ current_rate == 1.05")


@patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_rate_95_percent_do_nothing(mock_prediction: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing",\
        ("You should not sell cryptocurrency when prediction_rate "
         "/ current_rate == 0.95")
