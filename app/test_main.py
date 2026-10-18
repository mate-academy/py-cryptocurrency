from unittest.mock import MagicMock, patch
import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_action",
    [
        # Більше ніж +5% (> 1.05) -> Купувати
        (100.0, 105.1, "Buy more cryptocurrency"),
        (100.0, 110.0, "Buy more cryptocurrency"),
        # Менше ніж -5% (< 0.95) -> Продавати
        (100.0, 94.9, "Sell all your cryptocurrency"),
        (100.0, 90.0, "Sell all your cryptocurrency"),
        # Точно +5% (1.05) -> Нічого не робити
        (100.0, 105.0, "Do nothing"),
        # Точно -5% (0.95) -> Нічого не робити
        (100.0, 95.0, "Do nothing"),
        # У межах від -5% до +5% -> Нічого не робити
        (100.0, 100.0, "Do nothing"),
        (100.0, 104.9, "Do nothing"),
        (100.0, 95.1, "Do nothing"),
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

    assert main.cryptocurrency_action(current_rate) == expected_action
