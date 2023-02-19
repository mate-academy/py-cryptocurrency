from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.fixture
def mock_get_exchange_rate_prediction():
    with patch('app.main.get_exchange_rate_prediction') as mock_get_exchange_rate_prediction:
        yield mock_get_exchange_rate_prediction


def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 1.07
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 0.93
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing_when_1_05(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_when_0_95(mock_get_exchange_rate_prediction):
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"