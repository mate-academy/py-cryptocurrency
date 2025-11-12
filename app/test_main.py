import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing"),
        (100, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: MagicMock,
        predicted_rate: float,
        expected: str
) -> None:
    current_rate = 100
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected
