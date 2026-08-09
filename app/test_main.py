from typing import Generator

from unittest import mock

from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_get_exchange_rate_prediction() -> Generator:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mocked_prediction
    ):
        yield mocked_prediction


def test_for_using_func(mocked_get_exchange_rate_prediction: Mock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 20
    cryptocurrency_action(10)
    mocked_get_exchange_rate_prediction.assert_called_once()


def test_for_buying(mocked_get_exchange_rate_prediction: Mock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 20
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_for_selling(mocked_get_exchange_rate_prediction: Mock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 10
    assert cryptocurrency_action(20) == "Sell all your cryptocurrency"


def test_for_doing_nothing(mocked_get_exchange_rate_prediction: Mock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"


def test_for_doing_nothing_plus_five(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


def test_for_doing_nothing_minus_five(
        mocked_get_exchange_rate_prediction: Mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
