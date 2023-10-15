from typing import Union
from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.fixture
def mock_exchange_rate_prediction() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_cryptocurrency_action_buy(
        mock_exchange_rate_prediction: Union[int, float]) -> None:
    mock_exchange_rate_prediction.return_value = 1.5 * 100
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell(
        mock_exchange_rate_prediction: Union[int, float]) -> None:
    mock_exchange_rate_prediction.return_value = 0.9 * 100
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing_95(
        mock_exchange_rate_prediction: Union[int, float]) -> None:
    mock_exchange_rate_prediction.return_value = 0.95 * 100
    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action_do_nothing_105(
        mock_exchange_rate_prediction: Union[int, float]) -> None:
    mock_exchange_rate_prediction.return_value = 1.05 * 100
    assert cryptocurrency_action(100) == "Do nothing"
