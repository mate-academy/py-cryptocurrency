from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy(mock_pred: MagicMock) -> None:
    """Test buying cryptocurrency when the predicted rate increases."""
    mock_pred.return_value = 110

    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell(mock_pred: MagicMock) -> None:
    """Test selling cryptocurrency when the predicted rate decreases."""
    mock_pred.return_value = 0

    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_pred: MagicMock) -> None:
    """Test doing nothing when the predicted rate changes slightly."""
    mock_pred.return_value = 103

    result = cryptocurrency_action(100)

    assert result == "Do nothing"
