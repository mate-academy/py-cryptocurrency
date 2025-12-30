from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_when_prediction_more_than_5_percent_higher(
    mock_prediction: MagicMock,
) -> None:
    """Test that function returns 'Buy more cryptocurrency' when >5% higher"""
    mock_prediction.return_value = 110.0  # 10% higher than 100
    result = cryptocurrency_action(100.0)
    assert result == "Buy more cryptocurrency"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_when_prediction_more_than_5_percent_lower(
    mock_prediction: MagicMock,
) -> None:
    """Test that function returns 'Sell all' when prediction is >5% lower"""
    mock_prediction.return_value = 90.0  # 10% lower than 100
    result = cryptocurrency_action(100.0)
    assert result == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_within_5_percent_range(
    mock_prediction: MagicMock,
) -> None:
    """Test that function returns 'Do nothing' when within ±5% range"""
    mock_prediction.return_value = 102.0  # 2% higher, within range
    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_exactly_5_percent_higher(
    mock_prediction: MagicMock,
) -> None:
    """Test boundary: exactly 5% higher should return 'Do nothing'"""
    mock_prediction.return_value = 105.0  # Exactly 5% higher
    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_exactly_5_percent_lower(
    mock_prediction: MagicMock,
) -> None:
    """Test boundary: exactly 5% lower should return 'Do nothing'"""
    mock_prediction.return_value = 95.0  # Exactly 5% lower
    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_when_prediction_just_above_5_percent_higher(
    mock_prediction: MagicMock,
) -> None:
    """Test boundary: just above 5% higher should return 'Buy more'"""
    mock_prediction.return_value = 105.01  # Just above 5% higher
    result = cryptocurrency_action(100.0)
    assert result == "Buy more cryptocurrency"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_when_prediction_just_below_5_percent_lower(
    mock_prediction: MagicMock,
) -> None:
    """Test boundary: just below 5% lower should return 'Sell all'"""
    mock_prediction.return_value = 94.99  # Just below 5% lower
    result = cryptocurrency_action(100.0)
    assert result == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_equals_current_rate(
    mock_prediction: MagicMock,
) -> None:
    """Test when prediction equals current rate"""
    mock_prediction.return_value = 100.0
    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(100.0)


@patch("app.main.get_exchange_rate_prediction")
def test_with_different_current_rates(mock_prediction: MagicMock) -> None:
    """Test with different current rate values"""
    # Test with integer
    mock_prediction.return_value = 220.0  # 10% higher
    result = cryptocurrency_action(200)
    assert result == "Buy more cryptocurrency"

    # Test with float
    mock_prediction.return_value = 45.0  # 10% lower
    result = cryptocurrency_action(50.0)
    assert result == "Sell all your cryptocurrency"
