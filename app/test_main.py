import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: object,
    current_rate: int,
    prediction: float,
    result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == result
