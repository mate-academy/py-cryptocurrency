# write your code here
from unittest import mock
import pytest
from typing import Any
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "predicted,current,expected",
    [
        (106, 100, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
    ],
)
def test_cryptocurrency_action(mock_prediction: Any,
                               predicted: int,
                               current: int,
                               expected: str
                               ) -> None:
    mock_prediction.return_value = predicted
    result = cryptocurrency_action(current_rate=current)
    assert result == expected
