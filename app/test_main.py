from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_when_prediction_more_than_5_percent_higher(
        mock_prediction: MagicMock
) -> None:
    """Test buying when predicted rate is more than 5% higher"""
    current_rate = 100
    mock_prediction.return_value = 106  # Exactly 6% higher

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency_when_prediction_more_than_5_percent_lower(
        mock_prediction: MagicMock
) -> None:
    """Test selling when predicted rate is more than 5% lower"""
    current_rate = 100
    mock_prediction.return_value = 94  # Exactly 6% lower

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_exactly_5_percent_higher(
        mock_prediction: MagicMock
) -> None:
    """Test boundary: exactly 5% higher should do nothing"""
    current_rate = 100
    mock_prediction.return_value = 105  # Exactly 5% higher

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_exactly_5_percent_lower(
        mock_prediction: MagicMock
) -> None:
    """Test boundary: exactly 5% lower should do nothing"""
    current_rate = 100
    mock_prediction.return_value = 95  # Exactly 5% lower

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_slightly_higher(
        mock_prediction: MagicMock
) -> None:
    """Test doing nothing when predicted rate is slightly higher"""
    current_rate = 100
    mock_prediction.return_value = 102  # 2% higher

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_slightly_lower(
        mock_prediction: MagicMock
) -> None:
    """Test doing nothing when predicted rate is slightly lower"""
    current_rate = 100
    mock_prediction.return_value = 98  # 2% lower

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_same_as_current(
        mock_prediction: MagicMock
) -> None:
    """Test doing nothing when predicted rate equals current rate"""
    current_rate = 100
    mock_prediction.return_value = 100  # No change

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_buy_with_float_current_rate(
        mock_prediction: MagicMock
) -> None:
    """Test buying with float current rate"""
    current_rate = 50.5
    mock_prediction.return_value = 53.53  # More than 5% higher

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_sell_with_float_current_rate(
        mock_prediction: MagicMock
) -> None:
    """Test selling with float current rate"""
    current_rate = 50.5
    mock_prediction.return_value = 47.97  # More than 5% lower

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_buy_with_large_increase(
        mock_prediction: MagicMock
) -> None:
    """Test buying when predicted rate is significantly higher"""
    current_rate = 100
    mock_prediction.return_value = 200  # 100% increase

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_sell_with_large_decrease(
        mock_prediction: MagicMock
) -> None:
    """Test selling when predicted rate is significantly lower"""
    current_rate = 100
    mock_prediction.return_value = 50  # 50% decrease

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_buy_just_above_threshold(
        mock_prediction: MagicMock
) -> None:
    """Test buying when predicted rate is just above 5% threshold"""
    current_rate = 100
    mock_prediction.return_value = 105.01  # Just above 5%

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction")
def test_sell_just_below_threshold(
        mock_prediction: MagicMock
) -> None:
    """Test selling when predicted rate is just below 5% threshold"""
    current_rate = 100
    mock_prediction.return_value = 94.99  # Just below 5%

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)
