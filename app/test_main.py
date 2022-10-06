from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_positive(mock_random):
    mock_random.return_value = 150.01
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_negative(mock_random):
    mock_random.return_value = 94.99
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_neutral_if_lower(mock_random):
    mock_random.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_neutral_if_upper(mock_random):
    mock_random.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
