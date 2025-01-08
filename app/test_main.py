import pytest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,expected_result",
    [
        (1, 2, "Buy more cryptocurrency"),
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 0.5, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
    ]
)

@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: MagicMock,
        current_rate: float | int,
        exchange_rate: float | int,
        expected_result: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result