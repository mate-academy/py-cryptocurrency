import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100.0, 105.1, "Buy more cryptocurrency"),
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.9, "Sell all your cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 104.9, "Do nothing"),
        (100.0, 95.1, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),

    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_rate: MagicMock,
        current_rate: float,
        predicted_rate: float,
        expected_result: str
) -> None:
    mock_exchange_rate.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
