import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, action",
    [
        (110, "Buy more cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_buy_if_rate_is_higher(
    mocked_prediction: patch,
    predicted_rate: int | float,
    action: str
) -> None:
    mocked_prediction.return_value = predicted_rate
    assert cryptocurrency_action(100) == action
