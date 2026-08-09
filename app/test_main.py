import pytest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, expected",
    [
        (100, "Do nothing"),
        (95, "Do nothing"),
        (105, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
        (106, "Buy more cryptocurrency"),
        (94.99, "Sell all your cryptocurrency"),
        (105.01, "Buy more cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_get_prediction(
        rate_prediction: MagicMock,
        prediction_rate: int | float,
        expected: str
) -> None:
    rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(100)
    assert result == expected
