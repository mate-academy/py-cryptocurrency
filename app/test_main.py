from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_prediction: [int, float]) -> None:
    mock_get_prediction.return_value = 120
    current_rate = 100
    expected_output = "Buy more cryptocurrency"
    assert cryptocurrency_action(current_rate) == expected_output


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_prediction: [int, float]) -> None:
    mock_get_prediction.return_value = 80
    current_rate = 100
    expected_output = "Sell all your cryptocurrency"
    assert cryptocurrency_action(current_rate) == expected_output


@patch("app.main.get_exchange_rate_prediction")
def test_no_buy(mock_get_prediction: [int, float]) -> None:
    mock_get_prediction.return_value = 105
    current_rate = 100
    expected_output = "Do nothing"
    assert cryptocurrency_action(current_rate) == expected_output


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_prediction: [int, float]) -> None:
    mock_get_prediction.return_value = 95
    current_rate = 100
    expected_output = "Do nothing"
    assert cryptocurrency_action(current_rate) == expected_output
