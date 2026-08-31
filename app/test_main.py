from unittest.mock import MagicMock, patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100.0, 105.01, "Buy more cryptocurrency"),
        (100.0, 120.0, "Buy more cryptocurrency"),
        (100.0, 94.99, "Sell all your cryptocurrency"),
        (100.0, 80.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 102.0, "Do nothing"),
        (100.0, 97.0, "Do nothing"),
    ],
    ids=[
        "buy_above_5_percent_threshold",
        "buy_significant_increase",
        "sell_below_5_percent_threshold",
        "sell_significant_decrease",
        "boundary_exact_5_percent_increase",
        "boundary_exact_5_percent_decrease",
        "no_rate_change",
        "within_range_minor_increase",
        "within_range_minor_decrease",
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected_action: str,
) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action
