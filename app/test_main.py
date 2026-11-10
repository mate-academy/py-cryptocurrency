import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 110.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 90.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 104.0, "Do nothing"),
        (100.0, 96.0, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ) as mock_prediction:
        result: str = cryptocurrency_action(current_rate)

    assert result == expected
    mock_prediction.assert_called_once()
