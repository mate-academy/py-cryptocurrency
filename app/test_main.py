from unittest import mock
from unittest.mock import MagicMock
from collections.abc import Generator
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Generator[MagicMock, None, None]:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_exchange_rate
    ):
        mock_exchange_rate.return_value = 1.1
        yield mock_exchange_rate


def test_cryptocurrency_action_when_prediction_rate_big(
    mocked_get_exchange_rate_prediction: MagicMock
) -> None:
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_when_prediction_rate_small(
    mocked_get_exchange_rate_prediction: MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.2
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_when_prediction_rate_is_one(
    mocked_get_exchange_rate_prediction: MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.0
    assert cryptocurrency_action(1) == "Do nothing"


def test_returns_do_nothing_at_upper_boundary(
    mocked_get_exchange_rate_prediction: MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_returns_do_nothing_at_lower_boundary(
    mocked_get_exchange_rate_prediction: MagicMock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
