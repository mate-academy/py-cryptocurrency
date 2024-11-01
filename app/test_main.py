import pytest

from unittest import mock
from app.main import cryptocurrency_action
from typing import Union, Callable


@pytest.mark.parametrize(
    "test_rate, expected",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_rate_prediction: Callable,
        test_rate: Union[int, float],
        expected: str,
) -> None:
    mock_rate_prediction.return_value = test_rate
    assert cryptocurrency_action(1) == expected
