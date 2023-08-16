from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, result",
    [
        (100, 100, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 99, "Do nothing"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 110, "Buy more cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        moke_get_exchange_rate_prediction: int,
        current_rate: int,
        predicted_rate: int,
        result: str
) -> None:
    moke_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == result
