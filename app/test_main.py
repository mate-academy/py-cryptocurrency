import pytest
from unittest.mock import Mock
import app
from app.main import cryptocurrency_action

app.main.get_exchange_rate_prediction = Mock()


@pytest.mark.parametrize(
    "test_input,prediction_rate,expected",
    [
        (0.95, 0.1, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 1.95, "Buy more cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    test_input: int | float, prediction_rate: int | float, expected: str
) -> None:
    app.main.get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(test_input) == expected
