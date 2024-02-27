import pytest
from unittest import mock
from typing import Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction() -> None:
    path = "app.main.get_exchange_rate_prediction"
    with mock.patch(path) as mock_rate_prediction:
        yield mock_rate_prediction


def test_func_get_exchange_rate_prediction_was_called(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    cryptocurrency_action(1)
    mock_get_exchange_rate_prediction.assert_called_once_with(1)


def test_should_work_with_float_value(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    cryptocurrency_action(1.06)
    mock_get_exchange_rate_prediction.assert_called_once_with(1.06)


def test_should_return_buy_more_cryptocurrency_if_rate_greater_1_06(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 2
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_should_return_sell_all_if_rate_less_0_94(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_should_return_do_nothing_if_rate_less_0_95(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing_if_rate_greater_1_05(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_raises_type_error_if_value_not_integer_or_float() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("")


def test_raises_zero_division_error_if_value_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
