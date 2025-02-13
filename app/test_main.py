from app.main import cryptocurrency_action
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_predicion_high() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106):
        yield


@pytest.fixture
def mock_prediction_low() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94):
        yield


@pytest.fixture
def mock_prediction_same() -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=100):
        yield


def test_should_buy_more(mock_prediction_high: None) -> None:
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_should_sell_all(mock_prediction_low: None) -> None:
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_do_nothing(mock_prediction_same: None) -> None:
    assert cryptocurrency_action(100) == "Do nothing"
