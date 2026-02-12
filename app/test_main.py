from typing import Generator
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def current_rate() -> int:
    return 100


@pytest.fixture
def mocked_prediction() -> Generator[MagicMock, None, None]:
    with mock.patch("app.main.get_exchange_rate_prediction") as m:
        yield m


def test_should_buy_when_prediction_more_than_5_percent(
    mocked_prediction: MagicMock,
    current_rate: int,
) -> None:
    mocked_prediction.return_value = 106
    assert cryptocurrency_action(
        current_rate
    ) == "Buy more cryptocurrency"
    mocked_prediction.assert_called_once_with(current_rate)


def test_should_sell_when_prediction_less_than_5_percent(
    mocked_prediction: MagicMock,
    current_rate: int,
) -> None:
    mocked_prediction.return_value = 94
    assert cryptocurrency_action(
        current_rate
    ) == "Sell all your cryptocurrency"
    mocked_prediction.assert_called_once_with(current_rate)


def test_should_do_nothing_when_difference_less_than_5_percent(
    mocked_prediction: MagicMock,
    current_rate: int,
) -> None:
    mocked_prediction.return_value = 103
    assert cryptocurrency_action(current_rate) == "Do nothing"
    mocked_prediction.assert_called_once_with(current_rate)


def test_should_do_nothing_when_exactly_plus_5_percent(
    mocked_prediction: MagicMock,
    current_rate: int,
) -> None:
    mocked_prediction.return_value = 105
    assert cryptocurrency_action(current_rate) == "Do nothing"
    mocked_prediction.assert_called_once_with(current_rate)


def test_should_do_nothing_when_exactly_minus_5_percent(
    mocked_prediction: MagicMock,
    current_rate: int,
) -> None:
    mocked_prediction.return_value = 95
    assert cryptocurrency_action(current_rate) == "Do nothing"
    mocked_prediction.assert_called_once_with(current_rate)
