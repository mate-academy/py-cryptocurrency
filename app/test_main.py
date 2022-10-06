from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_func():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_exchange:
        yield mocked_exchange


def test_predicted_exchange_rate_is_more_than_5_higher(mocked_func):
    mocked_func.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_predicted_exchange_rate_is_more_than_5_lower(mocked_func):
    mocked_func.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_difference_is_not_that_much(mocked_func):
    mocked_func.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_difference_is_not_that_much_one_more(mocked_func):
    mocked_func.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
