from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_coin(mock_exchange_rate: Mock) -> None:
    mock_exchange_rate.return_value = 1.10

    actual_result = cryptocurrency_action(1.00)
    assert actual_result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_coin(mock_exchange_rate: Mock) -> None:
    mock_exchange_rate.return_value = 0.90

    actual_result = cryptocurrency_action(1.00)
    assert actual_result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_max_current_rate(mock_exchange_rate: Mock) -> None:
    mock_exchange_rate.return_value = 1.05

    actual_result = cryptocurrency_action(1.00)
    assert actual_result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_min_current_rate(mock_exchange_rate: Mock) -> None:
    mock_exchange_rate.return_value = 0.95

    actual_result = cryptocurrency_action(1.00)
    assert actual_result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_just_over_threshold(mock_exchange_rate: Mock) -> None:
    mock_exchange_rate.return_value = 1.0501

    actual_result = cryptocurrency_action(1.00)
    assert actual_result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_just_under_threshold(mock_exchange_rate: Mock) -> None:
    mock_exchange_rate.return_value = 0.9499

    actual_result = cryptocurrency_action(1.00)
    assert actual_result == "Sell all your cryptocurrency"
