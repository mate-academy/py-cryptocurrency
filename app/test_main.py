import pytest
from unittest import mock
from unittest.mock import MagicMock
from typing import Generator

from app import main


@pytest.fixture
def mock_get_exchange_rate_prediction() -> Generator:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange:
        yield mock_get_exchange


def test_cryptocarensy_strategy_if_exchange_rate_increase(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.1

    assert main.cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocarensy_strategy_if_exchange_rate_decrease(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.9

    assert main.cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocarensy_strategy_if_difference_not_to_much(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.0

    assert main.cryptocurrency_action(1) == "Do nothing"


@pytest.mark.parametrize("prediction_value", [0.95, 1.05])
def test_cryptocarensy_strategy_whith_limit_values(
    mock_get_exchange_rate_prediction: MagicMock, prediction_value: float
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_value

    assert main.cryptocurrency_action(1) == "Do nothing"
