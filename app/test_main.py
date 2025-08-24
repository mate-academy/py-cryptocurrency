from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


def calculate_predicted(current_rate: float, percentage: float) -> float:
    return current_rate * (1 + percentage / 100)


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100
    predicted_rate = calculate_predicted(current_rate, 6.0)
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100
    predicted_rate = calculate_predicted(current_rate, -6.0)
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_within_5_percent_increase(
    mock_prediction: Mock,
) -> None:
    current_rate = 100
    predicted_rate = calculate_predicted(current_rate, 4.9)
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_within_5_percent_decrease(
    mock_prediction: Mock,
) -> None:
    current_rate = 100
    predicted_rate = calculate_predicted(current_rate, -4.9)
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exactly_5_percent_increase(
    mock_prediction: Mock,
) -> None:
    current_rate = 100
    predicted_rate = calculate_predicted(current_rate, 5.0)
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exactly_5_percent_decrease(
    mock_prediction: Mock,
) -> None:
    current_rate = 100
    predicted_rate = calculate_predicted(current_rate, -5.0)
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
