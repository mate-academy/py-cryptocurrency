from unittest import mock
from app.main import cryptocurrency_action


@mock.patch('app.main.get_exchange_rate_prediction')
def test_cryptocurrency_action(mock_get_prediction: mock.Mock):

    mock_get_prediction.return_value = 1.11
    assert cryptocurrency_action(1.05) == "Buy more cryptocurrency"

    mock_get_prediction.return_value = 0.90
    assert cryptocurrency_action(1.05) == "Sell all your cryptocurrency"

    mock_get_prediction.return_value = 1.05
    assert cryptocurrency_action(1.00) == "Do nothing"

    mock_get_prediction.return_value = 0.95
    assert cryptocurrency_action(1.00) == "Do nothing"
