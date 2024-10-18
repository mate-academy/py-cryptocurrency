from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,mocked_value,result",
    [
        (1, 1, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (2, 0.1, "Sell all your cryptocurrency"),
        (0.5, 1.05, "Buy more cryptocurrency"),
        (0.5, 0.95, "Buy more cryptocurrency"),
    ],
    ids=[
        "difference is not that much",
        "difference is not that much",
        "difference is not that much",
        "predicted exchange rate is more than 5% lower from the current",
        "predicted exchange rate is more than 5% lower from the current",
        "predicted exchange rate is more than 5% higher from the current",
        "predicted exchange rate is more than 5% higher from the current",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: MagicMock,
        current_rate: int | float,
        mocked_value: int | float,
        result: str
) -> None:
    mocked_prediction.return_value = mocked_value
    assert cryptocurrency_action(current_rate) == result
