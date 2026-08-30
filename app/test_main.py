from unittest import mock
from unittest.mock import MagicMock
from typing import Generator

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Generator[MagicMock, None, None]:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange):
        yield mocked_get_exchange


def test_should_call_function_get_exchange_with_correct_value(
        mocked_get_exchange_rate_prediction: MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 400
    cryptocurrency_action(200)
    mocked_get_exchange_rate_prediction.assert_called_once_with(200)


def test_should_return_buy_more_crypto_currency_if_increase(
        mocked_get_exchange_rate_prediction: MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 10
    result = cryptocurrency_action(5)
    assert result == "Buy more cryptocurrency"


def test_should_return_sell_if_decrease(
        mocked_get_exchange_rate_prediction: MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 5
    result = cryptocurrency_action(10)
    assert result == "Sell all your cryptocurrency"


def test_should_return_do_nothing(
        mocked_get_exchange_rate_prediction: MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 5.25
    result = cryptocurrency_action(5)
    assert result == "Do nothing"


def test_check_bordered_value_if_increase(
        mocked_get_exchange_rate_prediction: MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 5.31

    result = cryptocurrency_action(5)
    assert result == "Buy more cryptocurrency"


def test_check_bordered_value_for_95_percent(
        mocked_get_exchange_rate_prediction: MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 4.75

    result = cryptocurrency_action(5)
    assert result == "Do nothing"


def test_check_bordered_value_for_94_percent(
        mocked_get_exchange_rate_prediction: MagicMock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 4.7

    result = cryptocurrency_action(5)
    assert result == "Sell all your cryptocurrency"
