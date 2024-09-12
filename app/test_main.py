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


def test_for_do_nothing(mocked_cryptocurrency_action):
    mocked_cryptocurrency_action.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"
    mocked_cryptocurrency_action.return_value = 249.85
    assert cryptocurrency_action(263) == "Do nothing"


def test_for_buy_cryptocurrency(mocked_cryptocurrency_action):
    mocked_cryptocurrency_action.return_value = 25.44
    assert cryptocurrency_action(24) == "Buy more cryptocurrency"


def test_for_sell_cryptocurrency(mocked_cryptocurrency_action):
    mocked_cryptocurrency_action.return_value = 118.44
    assert cryptocurrency_action(126) == "Sell all your cryptocurrency"
