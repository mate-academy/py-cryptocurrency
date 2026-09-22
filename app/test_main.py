from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction_rate,current_rate,message",
    [
        (106, 100, "Buy more cryptocurrency"),
        (101, 100, "Do nothing"),
        (94, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
    ],
    ids=[
        "more than 5% higher from the current",
        "between 5% higher and 5% lower",
        "more than 5% lower",
        "5% higher",
        "5% lower",
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def testt_buy_more_cryptocurrency(
    mock_get_exchange_prediction: MagicMock,
    prediction_rate: int,
    current_rate: int,
    message: str,
) -> None:
    mock_get_exchange_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == message
