from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.fixture()
def mocked_get():
    with mock.patch("app.main.get_exchange_rate_prediction") as mmm:
        yield mmm


def test_cryptocurrency_action_higger(mocked_get):
    mocked_get.return_value = 1.05
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_lower(mocked_get):
    mocked_get.return_value = 0.95
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_some(mocked_get):
    mocked_get.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"
