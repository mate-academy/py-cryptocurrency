from __future__ import annotations
from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,rate_prediction,expected_action",
    [
        (1, 2.2, "Buy more cryptocurrency"),
        (2.2, 1, "Sell all your cryptocurrency"),
        (2.2, 2.1, "Do nothing"),
        (2.1, 2, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock.MagicMock,
        current_rate: int | float,
        rate_prediction: int | float,
        expected_action: str
) -> None:
    mocked_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(current_rate) == expected_action