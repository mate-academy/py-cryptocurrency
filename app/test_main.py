import pytest
from unittest.mock import patch, MagicMock
import app.main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        current_rate: int,
        predicted_rate: int,
        expected_action: str
) -> None:
    mock_prediction.return_value = predicted_rate

    result = app.main.cryptocurrency_action(current_rate)

    assert result == expected_action
