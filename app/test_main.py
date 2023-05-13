import pytest
from app.main import cryptocurrency_action, get_exchange_rate_prediction
from unittest import mock


@pytest.fixture()
def mocked_get_exchange_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_prediction:
        yield mock_prediction


def test_cryptocurrency_action_buy(mocked_get_exchange_rate_prediction):
    current_rate = 1
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell(mocked_get_exchange_rate_prediction):
    current_rate = 1
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_nothing(mocked_get_exchange_rate_prediction):
    current_rate = 1
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_cryptocurrency_action_nothing_0_95(mocked_get_exchange_rate_prediction):
    current_rate = 1
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_cryptocurrency_action_nothing_1_05(mocked_get_exchange_rate_prediction):
    current_rate = 1
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(current_rate) == "Do nothing"
