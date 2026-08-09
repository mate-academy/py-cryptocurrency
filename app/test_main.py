from unittest.mock import patch, MagicMock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 102, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_scenarios(
        mock_pred: MagicMock,
        current_rate: float | int,
        predicted_rate: float | int ,
        expected: str
) -> None:
    mock_pred.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
