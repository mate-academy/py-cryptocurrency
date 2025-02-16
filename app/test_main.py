from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_get_exchange_rate_prediction: patch
) -> None:
    """Test when predicted rate is more than 5% higher."""
    current_rate: float = 100
    mock_get_exchange_rate_prediction.return_value = 106  # +6%

    result: str = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mock_get_exchange_rate_prediction: patch
) -> None:
    """Test when predicted rate is more than 5% lower."""
    current_rate: float = 100
    mock_get_exchange_rate_prediction.return_value = 94  # -6%

    result: str = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_upper_boundary(
    mock_get_exchange_rate_prediction: patch
) -> None:
    """Test when predicted rate is exactly 5% higher."""
    current_rate: float = 100
    mock_get_exchange_rate_prediction.return_value = 105  # +5%

    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lower_boundary(
    mock_get_exchange_rate_prediction: patch
) -> None:
    """Test when predicted rate is exactly 5% lower."""
    current_rate: float = 100
    mock_get_exchange_rate_prediction.return_value = 95  # -5%

    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_small_variation(
    mock_get_exchange_rate_prediction: patch
) -> None:
    """Test when predicted rate changes by less than 5%."""
    current_rate: float = 100
    mock_get_exchange_rate_prediction.return_value = 102  # +2%

    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_slight_decrease(
    mock_get_exchange_rate_prediction: patch
) -> None:
    """Test when predicted rate decreases by less than 5%."""
    current_rate: float = 100
    mock_get_exchange_rate_prediction.return_value = 98  # -2%

    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
