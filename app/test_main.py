from unittest import mock
from app.main import cryptocurrency_action


@mock.patch('app.main.get_exchange_rate_prediction')
class TestActionCalls:
    def test_sell(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 9
        assert cryptocurrency_action(10) == "Sell all your cryptocurrency"

    def test_buy(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 10.2
        assert cryptocurrency_action(2.3) == "Buy more cryptocurrency"

    def test_hold(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 8
        assert cryptocurrency_action(8) == "Do nothing"
        mock_exchange_rate_prediction.return_value = 10
        assert cryptocurrency_action(10 / 0.95) == "Do nothing"
        assert cryptocurrency_action(10 / 1.05) == "Do nothing"
