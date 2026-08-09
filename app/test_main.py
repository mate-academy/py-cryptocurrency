from typing import Any
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mock_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction):
        yield mocked_prediction


def test_cryptocurrency_action_when_prediction_rate_is_positive(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 106
    result = cryptocurrency_action(100)
    mock_prediction.assert_called_once_with(100)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_when_prediction_rate_is_negative(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94
    result = cryptocurrency_action(100)
    mock_prediction.assert_called_once_with(100)
    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_when_prediction_rate_is_neutral(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 100
    result = cryptocurrency_action(100)
    mock_prediction.assert_called_once_with(100)
    assert result == "Do nothing"


def test_cryptocurrency_action_when_prediction_rate_is_1_05(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(100)
    mock_prediction.assert_called_once_with(100)
    assert result == "Do nothing"


def test_cryptocurrency_action_when_prediction_rate_is_0_95(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(100)
    mock_prediction.assert_called_once_with(100)
    assert result == "Do nothing"
