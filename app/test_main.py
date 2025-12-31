from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_prediction):
    mock_prediction.return_value = 105.1
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_prediction):
    mock_prediction.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_upper_boundary(mock_prediction):
    mock_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_lower_boundary(mock_prediction):
    mock_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_equal(mock_prediction):
    mock_prediction.return_value = 100.0
    assert cryptocurrency_action(100) == "Do nothing"
