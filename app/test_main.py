from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,expected_result",
    [
        (5 / 1.05, "Do nothing"),
        (5 / 1.05 - 0.0001, "Buy more cryptocurrency"),
        (5 / 0.95, "Do nothing"),
        (5 / 0.95 + 0.0001, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_boundaries(
        mocked_exchange_rate_prediction: MagicMock,
        current_rate: float,
        expected_result: str,
) -> None:
    mocked_exchange_rate_prediction.return_value = 5
    assert cryptocurrency_action(current_rate) == expected_result
