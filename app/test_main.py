import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected",
                         [
                             (1, 2, "Buy more cryptocurrency"),
                             (1, 0.5, "Sell all your cryptocurrency"),
                             (1, 0.95, "Do nothing"),
                             (1, 1.05, "Do nothing")
                         ])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction: MagicMock,
                               current_rate: float,
                               predicted_rate: float,
                               expected: str) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
