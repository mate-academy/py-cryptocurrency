# write your code here
from unittest import mock
from unittest.mock import MagicMock, AsyncMock

import pytest
from typing import Any, Generator
from app.main import cryptocurrency_action


@pytest.fixture
def mocked_exchange_rate() -> Generator[MagicMock | AsyncMock, Any, None]:
    with mock.patch("app.main.get_exchange_rate_prediction") as test_rate:
        yield test_rate


def test_return_more_if_rate_big_enough(
        mocked_exchange_rate: MagicMock
) -> None:
    mocked_exchange_rate.return_value = 3
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_return_sell_if_rate_small_enough(
        mocked_exchange_rate: MagicMock
) -> None:
    mocked_exchange_rate.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_return_nothing_if_rate_has_no_difference(
        mocked_exchange_rate: MagicMock
) -> None:
    mocked_exchange_rate.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_95_percent_do_nothing(
        mocked_exchange_rate: MagicMock
) -> None:
    mocked_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_105_percent_do_nothing(
        mocked_exchange_rate: MagicMock
) -> None:
    mocked_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
