from typing import Any, Generator
from unittest import mock
from unittest.mock import MagicMock, AsyncMock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_prediction() -> Generator[MagicMock | AsyncMock, Any, None]:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        pytest.param(
            100,
            100,
            "Do nothing",
            id="same current and predicted rate, no action is required"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="predicted rate higher, no action is required"
        ),
        pytest.param(
            100,
            106,
            "Buy more cryptocurrency",
            id="predicted rate higher, action is needed"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="predicted rate lower, no action is required"
        ),
        pytest.param(
            100,
            94,
            "Sell all your cryptocurrency",
            id="predicted rate lower, action is needed"
        ),
    ]
)
def test_return_action_correctly(
        current_rate: int | float,
        predicted_rate: int | float,
        expected_action: str,
        mock_prediction: MagicMock | AsyncMock
) -> None:
    mock_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action


def test_should_request_prediction(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 150
    cryptocurrency_action(100)
    mock_prediction.assert_called_once_with(100)
