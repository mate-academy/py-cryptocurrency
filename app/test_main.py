import pytest
from app.main import cryptocurrency_action
from unittest import mock
from typing import Callable


@pytest.fixture()
def mock_prediction() -> Callable:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        yield mocked_prediction


def test_cryptocurrency_action_with_better_rate(
        mock_prediction: Callable
) -> None:
    mock_prediction.return_value = 1
    assert cryptocurrency_action(1.5) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_with_bad_rate(
        mock_prediction: Callable
) -> None:
    mock_prediction.return_value = 1.5
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_first_exception(
        mock_prediction: Callable
) -> None:
    mock_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_action_second_exception(
        mock_prediction: Callable
) -> None:
    mock_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
