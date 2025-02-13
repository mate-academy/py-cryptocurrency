from app.main import cryptocurrency_action
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_prediction_high() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=105):
        yield mock


@pytest.fixture
def mock_prediction_low() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95):
        yield mock


@pytest.fixture
def mock_prediction_same() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=100):
        yield mock


def test_should_buy_more(mock_prediction_high: None) -> None:
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_should_sell_all(mock_prediction_low: None) -> None:
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_do_nothing(mock_prediction_same: None) -> None:
    assert cryptocurrency_action(100) == "Do nothing"

@pytest.mark.parametrize("mock_prediction_value", [105, 95])
def test_should_do_nothing_on_boundary(mock_prediction_value: int) -> None:
    """Ensure that when prediction is exactly 1.05x or 0.95x, we do nothing"""
    with patch("app.main.get_exchange_rate_prediction", return_value=mock_prediction_value):
        assert cryptocurrency_action(100) == "Do nothing"