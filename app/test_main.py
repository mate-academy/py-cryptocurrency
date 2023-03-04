from app.main import cryptocurrency_action
from unittest import mock
import pytest
from typing import Callable


@pytest.fixture()
def mocked_func() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_rate_predict:
        yield mock_rate_predict


@pytest.mark.parametrize(
    "current_rate,current_predict,result",
    [
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 107, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency")
    ],
    ids=[
        "Do nothing",
        "Do nothing",
        "buy more",
        "sell all"
    ]
)
def test_crypro_currency_action(
        mocked_func: Callable,
        current_rate: int | float,
        current_predict: int | float,
        result: str
) -> None:
    mocked_func.return_value = current_predict
    assert cryptocurrency_action(current_rate) == result


def test_get_exchange_rate_prediction(mocked_func: Callable) -> None:
    mocked_func.return_value = 10
    cryptocurrency_action(2)
    mocked_func.assert_called_once_with(2)
