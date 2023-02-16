from app.main import get_exchange_rate_prediction, cryptocurrency_action
from unittest import mock


@mock.patch('app.main.get_exchange_rate_prediction', return_value=10.0)
def test_cryptocurrency_action_higher_5(exchange_function):
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


@mock.patch('app.main.get_exchange_rate_prediction', return_value=3.0)
def test_cryptocurrency_action_lower_5(exchange_function):
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


@mock.patch('app.main.get_exchange_rate_prediction', return_value=5.0)
def test_cryptocurrency_action_do_nothing(exchange_function):
    assert cryptocurrency_action(5) == "Do nothing"


