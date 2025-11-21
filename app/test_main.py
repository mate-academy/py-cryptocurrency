from unittest import mock
import pytest
from typing import Any

from app.main import cryptocurrency_action


@pytest.fixture
def mock_rate_prediction() -> Any:
    with mock.patch("app.main.get_exchange_rate_prediction") as predict_rate:
        yield predict_rate


def test_predict_action_buy(mock_rate_prediction: Any) -> None:
    mock_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_predict_action_sell(mock_rate_prediction: Any) -> None:
    mock_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_predict_action_do_nothing_low(mock_rate_prediction: Any) -> None:
    mock_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_predict_action_do_nothing_high(mock_rate_prediction: Any) -> None:
    mock_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
