from unittest.mock import patch, MagicMock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.buy
@pytest.mark.parametrize(
    "current_rate,predicted_rate",
    [
        (100, 106),
        (100, 105.01),
        (100.50, 106.53),
        (0.5, 0.53),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float) -> None:
    """Test buying when predicted rate is more than 5% higher."""
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@pytest.mark.sell
@pytest.mark.parametrize(
    "current_rate,predicted_rate",
    [
        (100, 94),
        (100, 94.99),
        (10000, 9400),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float) -> None:
    """Test selling when predicted rate is more than 5% lower."""
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"
    mock_prediction.assert_called_once_with(current_rate)


@pytest.mark.do_nothing
@pytest.mark.parametrize(
    "current_rate,predicted_rate",
    [
        (100, 100),
        (100, 103),
        (100, 97),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(
        mock_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float) -> None:
    """Test doing nothing when prediction is within 5% range."""
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
    mock_prediction.assert_called_once_with(current_rate)


@pytest.mark.boundary
@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_action",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_boundary_conditions(
        mock_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected_action: str) -> None:
    """Test exact boundary conditions at 5% threshold."""
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected_action
    mock_prediction.assert_called_once_with(current_rate)
