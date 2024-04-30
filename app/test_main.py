import pytest
from unittest import mock

from app.main import get_exchange_rate_prediction, cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate_prediction, result_action",
    [
        (25, 50, "Buy more cryptocurrency"),
        (100, 100 * 0.94, "Sell all your cryptocurrency"),
        (100, 100 * 1.05, "Do nothing"),
        (100, 100 * 0.95, "Do nothing"),
        (100, 100 * 1.06, "Buy more cryptocurrency"),
        (116, 100, "Sell all your cryptocurrency")
    ]
)
def test_action(
        current_rate: int,
        exchange_rate_prediction: int,
        result_action: str) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=exchange_rate_prediction
    ) as mocked_prediction:
        mocked_prediction(current_rate)
        assert cryptocurrency_action(current_rate) == result_action
