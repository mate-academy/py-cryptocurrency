from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_prediction_more_than_5_than_current(mock_prediction: float) -> None:
    mock_prediction.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_prediction_more_than_5_lower_current(mock_prediction: float) -> None:
    mock_prediction.return_value = 90
    result = cryptocurrency_action(95)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_prediction_not_much_difference(mock_prediction: float) -> None:
    mock_prediction.return_value = 96
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_prediction_105_percent_do_nothing(mock_prediction: float) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_prediction_95_percent_do_nothing(mock_prediction: float) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
