from unittest.mock import Mock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 106.0  # > 5% increase
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_cryptocurrency(mock_prediction: Mock) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 94.0  # > 5% decrease
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_if_change_is_small(mock_prediction: Mock) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 97.0  # within ±5%
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_if_exactly_5_percent_increase(
    mock_prediction: Mock,
) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 105.0  # exactly 5%
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_if_exactly_5_percent_decrease(
    mock_prediction: Mock,
) -> None:
    current_rate = 100.0
    mock_prediction.return_value = 95.0  # exactly -5%
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
