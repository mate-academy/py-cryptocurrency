from unittest import mock
from typing import Callable

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_rate_prediction() -> Callable:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_prediction:
        yield mock_prediction


def test_cryptocurrency_action_with_growth(
        mock_rate_prediction: Callable
) -> None:

    mock_rate_prediction.return_value = 20

    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_cryptocurrency_action_with_fall(
        mock_rate_prediction: Callable
) -> None:

    mock_rate_prediction.return_value = 10

    assert cryptocurrency_action(20) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_with_small_growth(
        mock_rate_prediction: Callable
) -> None:

    mock_rate_prediction.return_value = 5.25

    assert cryptocurrency_action(5) == "Do nothing"


def test_cryptocurrency_action_with_small_fall(
        mock_rate_prediction: Callable
) -> None:

    mock_rate_prediction.return_value = 4.75

    assert cryptocurrency_action(5) == "Do nothing"
