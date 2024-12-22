from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_prediction: patch) -> None:
    mock_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency",\
        "Should advise to buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_prediction: patch) -> None:
    mock_prediction.return_value = 90
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency",\
        "Should advise to sell all cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mock_prediction: patch) -> None:
    mock_prediction.return_value = 102
    result = cryptocurrency_action(100)
    assert result == "Do nothing",\
        "Should advise to do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_exact_current_rate(
        mock_prediction: patch
) -> None:
    mock_prediction.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing",\
        "Should advise to do nothing when rates are equal"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_prediction: patch) -> None:
    current_rate = 100
    mock_prediction.return_value = 95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_prediction: patch) -> None:
    current_rate = 100
    mock_prediction.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
