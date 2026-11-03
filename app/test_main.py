from unittest.mock import patch
import pytest

import app.main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        # Прогноз росте більше ніж на 5% -> Buy
        (100.0, 106.0, "Buy more cryptocurrency"),
        (200.0, 215.0, "Buy more cryptocurrency"),

        # Прогноз падає більше ніж на 5% -> Sell
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (200.0, 180.0, "Sell all your cryptocurrency"),

        # Різниця рівно 5% або менше -> Do nothing (граничні умови)
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 102.0, "Do nothing"),
        (100.0, 98.0, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: object,
        current_rate: float,
        predicted_rate: float,
        expected_action: str,
) -> None:
    mock_prediction.return_value = predicted_rate

    result = app.main.cryptocurrency_action(current_rate)
    assert result == expected_action
    mock_prediction.assert_called_once()
