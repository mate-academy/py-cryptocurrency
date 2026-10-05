from unittest.mock import patch, Mock
import pytest
from app import main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 105, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105.01, "Buy more cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_predict: Mock,
                               current_rate: float,
                               predicted_rate: float,
                               expected: str) -> None:
    mock_predict.return_value = predicted_rate
    assert main.cryptocurrency_action(current_rate) == expected
