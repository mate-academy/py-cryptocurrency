from unittest import mock
import pytest
from app.main import cryptocurrency_action
from typing import Callable, Union


@pytest.fixture()
def mocked_function() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        yield mocked


@pytest.mark.parametrize(
    "current,predict,result",
    [
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.07, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        mocked_function: Callable,
        current: Union[int, float],
        predict: Union[int, float],
        result: str
) -> None:
    mocked_function.return_value = predict
    assert cryptocurrency_action(current) == result
