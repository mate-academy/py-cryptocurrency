from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (50, 53, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (80, 75, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: MagicMock,
        current_rate: int | float,
        predicted_rate: int | float,
        result: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == result
