from __future__ import annotations
import pytest
from unittest import mock
from unittest.mock import MagicMock, AsyncMock
from typing import Generator
from app.main import cryptocurrency_action


@pytest.fixture
def mock_get_exchange_rate() -> Generator[MagicMock | AsyncMock]:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_exchange_rate:
        yield mocked_exchange_rate


def test_buy_more_when_prediction_rate_is_higher_than_current(
        mock_get_exchange_rate: MagicMock | AsyncMock
) -> None:
    mock_get_exchange_rate.return_value = 5.31
    assert cryptocurrency_action(3.18) == "Buy more cryptocurrency"


def test_sell_all_when_prediction_rate_is_lower_than_current(
        mock_get_exchange_rate: MagicMock | AsyncMock
) -> None:
    mock_get_exchange_rate.return_value = 5
    assert cryptocurrency_action(6.23) == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_rate_is_between_95_and_105_percent(
        mock_get_exchange_rate: MagicMock | AsyncMock
) -> None:
    mock_get_exchange_rate.return_value = 4.93
    assert cryptocurrency_action(4.75) == "Do nothing"


def test_do_nothing_when_prediction_rate_is_95_percent_of_current_(
        mock_get_exchange_rate: MagicMock | AsyncMock
) -> None:
    mock_get_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_when_prediction_rate_is_105_percent_of_current_(
        mock_get_exchange_rate: MagicMock | AsyncMock
) -> None:
    mock_get_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
