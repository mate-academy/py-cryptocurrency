from unittest.mock import patch, Mock
from app.main import get_exchange_rate_prediction, cryptocurrency_action


@patch("random.choice", return_value="increase")
@patch("random.random", return_value=0.5)
def test_prediction_increase(mock_random: Mock, mock_choice: Mock) -> None:
    result = get_exchange_rate_prediction(100)
    assert result == 200


@patch("random.choice", return_value="decrease")
@patch("random.random", return_value=0.5)
def test_prediction_decrease(mock_random: Mock, mock_choice: Mock) -> None:
    result = get_exchange_rate_prediction(100)
    assert result == 50


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_get_prediction: Mock) -> None:
    mock_get_prediction.return_value = 106
    action = cryptocurrency_action(100)
    assert action == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_get_prediction: Mock) -> None:
    mock_get_prediction.return_value = 94
    action = cryptocurrency_action(100)
    assert action == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_get_prediction: Mock) -> None:
    mock_get_prediction.return_value = 105
    action = cryptocurrency_action(100)
    assert action == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_get_prediction: Mock) -> None:
    mock_get_prediction.return_value = 95
    action = cryptocurrency_action(100)
    assert action == "Do nothing"
