from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,random_prediction,expected_action",
    [
        (1, 2, "Buy more cryptocurrency"),
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.5, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock.MagicMock,
        current_rate: int,
        random_prediction: Union[int, float],
        expected_action: str
) -> None:
    mocked_prediction.return_value = random_prediction
    assert cryptocurrency_action(current_rate) == expected_action
