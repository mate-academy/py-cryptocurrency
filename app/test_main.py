import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocket_random_function():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_action:
        yield mocked_action


def test_get_exchange_rate_prediction_called(mocket_random_function):
    mocket_random_function.return_value = 5
    cryptocurrency_action(5)
    mocket_random_function.assert_called_once()


def test_predicted_more_5pers_higher_current(mocket_random_function):
    mocket_random_function.return_value = 10
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_predicted_5pers_higher_current(mocket_random_function):
    mocket_random_function.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


def test_predicted_less_5pers_lower_current(mocket_random_function):
    mocket_random_function.return_value = 10
    assert cryptocurrency_action(1000) == "Sell all your cryptocurrency"


def test_predicted_5pers_lower_current(mocket_random_function):
    mocket_random_function.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"


def test_difference_is_small(mocket_random_function):
    mocket_random_function.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"
