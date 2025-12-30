import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Callable


@pytest.fixture()
def mocked_predict() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_prediction:
        yield mocked_prediction


def test_function_returns_buy(mocked_predict: Callable) -> None:
    mocked_predict.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_function_returns_sell(mocked_predict: Callable) -> None:
    mocked_predict.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_function_returns_do_nothing(mocked_predict: Callable) -> None:
    mocked_predict.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_function_returns_do_nothing_2(mocked_predict: Callable) -> None:
    mocked_predict.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_function_raises_error() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("1")
