import pytest
from unittest.mock import Mock, patch
from app.main import cryptocurrency_action


@pytest.fixture
def mock_exchange_rate() -> Mock:
    """Fixture to mock get_exchange_rate_prediction function"""
    with patch("app.main.get_exchange_rate_prediction") as mock_rate:
        yield mock_rate


def test_buy_when_rate_increases_above_5_percent(mock_exchange_rate
                                                 : Mock) -> None:
    """Test when predicted rate is more than 5% higher"""
    current_rate = 100.0
    predicted_rate = 105.1  # >5% increase
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_sell_when_rate_decreases_below_5_percent(mock_exchange_rate
                                                  : Mock) -> None:
    """Test when predicted rate is more than 5% lower"""
    current_rate = 100.0
    predicted_rate = 94.9  # >5% decrease
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_do_nothing_when_rate_within_5_percent(mock_exchange_rate
                                               : Mock) -> None:
    """Test when rate change is within 5% threshold"""
    current_rate = 100.0
    predicted_rate = 102.0  # 2% increase
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_boundary_at_5_percent_increase(mock_exchange_rate: Mock) -> None:
    """Test exactly 5% increase boundary condition"""
    current_rate = 100.0
    predicted_rate = 105.0  # Exactly 5% increase
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_boundary_at_5_percent_decrease(mock_exchange_rate: Mock) -> None:
    """Test exactly 5% decrease boundary condition"""
    current_rate = 100.0
    predicted_rate = 95.0  # Exactly 5% decrease
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_just_above_5_percent_increase(mock_exchange_rate: Mock) -> None:
    """Test just above 5% increase boundary"""
    current_rate = 100.0
    predicted_rate = 105.01  # Slightly more than 5% increase
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_just_below_5_percent_decrease(mock_exchange_rate: Mock) -> None:
    """Test just below 5% decrease boundary"""
    current_rate = 100.0
    predicted_rate = 94.99  # Slightly more than 5% decrease
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_integer_input(mock_exchange_rate: Mock) -> None:
    """Test function works with integer input"""
    current_rate = 100
    predicted_rate = 106  # >5% increase
    mock_exchange_rate.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"
