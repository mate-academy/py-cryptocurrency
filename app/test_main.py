from typing import Iterator
from unittest.mock import MagicMock, patch

import pytest

from app import main


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Iterator[MagicMock]:
    with patch("app.main.get_exchange_rate_prediction") as mock_test:
        yield mock_test


def test_buy_more_when_prediction_more_than_5_percent_higher(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 110

    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_when_prediction_more_than_5_percent_lower(
    mocked_get_exchange_rate_prediction: MagicMock,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 2

    assert main.cryptocurrency_action(4) == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "course,forecast",
    [
        pytest.param(100, 102, id="test when_small change"),
        pytest.param(100, 105, id="Exactly +5% (threshold)"),
        pytest.param(100, 95, id="Exactly −5% (threshold)"),
    ],
)
def test_do_nothing_when_change_within_5_percent(
    mocked_get_exchange_rate_prediction: MagicMock,
    course: int | float,
    forecast: int | float,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = forecast

    assert main.cryptocurrency_action(course) == "Do nothing"
