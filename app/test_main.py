from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_action",
    [
        (106.0, 100.0, "Buy more cryptocurrency"),
        (94.0, 100.0, "Sell all your cryptocurrency"),
        (100.0, 100.0, "Do nothing"),
        (105.0, 100.0, "Do nothing"),
        (95.0, 100.0, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: patch,
    prediction_rate: float,
    current_rate: float,
    expected_action: str,
) -> None:
    mock_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_action
