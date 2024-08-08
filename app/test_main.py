from typing import Callable

import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_prediction() -> Callable:
    with mock.patch("app.main.get_exchange_rate_prediction") as predict_mock:
        yield predict_mock


def test_cryptocurrency_higher_rate(
    mock_get_prediction: mock.MagicMock
) -> None:
    mock_get_prediction.return_value = 10.9
    result = cryptocurrency_action(10)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_low_rate(mock_get_prediction: mock.MagicMock) -> None:
    mock_get_prediction.return_value = 8
    result = cryptocurrency_action(10)
    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_no_significant_change(
    mock_get_prediction: mock.MagicMock
) -> None:
    mock_get_prediction.return_value = 9.5
    result = cryptocurrency_action(10)
    assert result == "Do nothing"
    mock_get_prediction.return_value = 10.5
    result = cryptocurrency_action(10)
    assert result == "Do nothing"
