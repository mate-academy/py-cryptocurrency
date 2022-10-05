import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_cryptocurrency_action():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_action:
        yield mocked_action


def test_should_call_function(mocked_cryptocurrency_action):
    mocked_cryptocurrency_action.return_value = 1.09
    cryptocurrency_action(1.09)
    mocked_cryptocurrency_action.assert_called()


def test_for_buy_cryptocurrency(mocked_cryptocurrency_action):
    mocked_cryptocurrency_action.return_value = 120
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_for_sell_cryptocurrency(mocked_cryptocurrency_action):
    mocked_cryptocurrency_action.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_for_do_nothing(mocked_cryptocurrency_action):
    mocked_cryptocurrency_action.return_value = 13
    assert cryptocurrency_action(12.7) == "Do nothing"

