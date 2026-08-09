from unittest import mock
import pytest
from app import main


DECISION = [
    (1.06, 1.00, "Buy more cryptocurrency"),
    (1.05, 1.00, "Do nothing"),
    (1.051, 1.00, "Buy more cryptocurrency"),
    (1.00, 1.00, "Do nothing"),
    (0.95, 1.00, "Do nothing"),
    (0.949, 10.0, "Sell all your cryptocurrency"),
    (0.94, 1.00, "Sell all your cryptocurrency"),
]


@pytest.mark.parametrize("prediction, current_rate, expected", DECISION)
def test_cryptocurrency_action(
    prediction: float,
    current_rate: float,
    expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = prediction
        result = main.cryptocurrency_action(current_rate)
        assert result == expected
