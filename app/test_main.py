from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_call_rate_prediction_with_given_value_once(
    mocked_rate_prediction: Mock
) -> None:
    mocked_rate_prediction.return_value = 1.32

    cryptocurrency_action(1.2)

    mocked_rate_prediction.assert_called_once_with(1.2)


def test_return_buy_more_if_prediction_favorable(
    mocked_rate_prediction: Mock
) -> None:
    mocked_rate_prediction.return_value = 1.27

    advise = cryptocurrency_action(1.2)

    assert advise == "Buy more cryptocurrency"


def test_return_sell_all_if_prediction_is_not_favorable(
    mocked_rate_prediction: Mock
) -> None:
    mocked_rate_prediction.return_value = 1.13

    advise = cryptocurrency_action(1.2)

    assert advise == "Sell all your cryptocurrency"


def test_return_do_nothing_if_it_makes_no_sense(
    mocked_rate_prediction: Mock
) -> None:
    mocked_rate_prediction.return_value = 1.14
    advise1 = cryptocurrency_action(1.2)
    mocked_rate_prediction.return_value = 1.26
    advise2 = cryptocurrency_action(1.2)

    assert advise1 == advise2 == "Do nothing"


def test_should_raise_type_error_if_not_int_or_float_is_given() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("123")


def test_should_always_raise_zero_division_error_0_is_given() -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
