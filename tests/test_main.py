from unittest import mock
from app.main import cryptocurrency_action


@mock.patch('app.main.get_exchange_rate_prediction')
class TestActionCalls:
    def test_call_to_buy_cryptocurrency(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 11
        assert cryptocurrency_action(10) == "Buy more cryptocurrency"

    def test_call_to_sell_cryptocurrency(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 9
        assert cryptocurrency_action(10) == "Sell all your cryptocurrency"

    def test_call_to_hold_cryptocurrency(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 10
        assert cryptocurrency_action(9.523809523809524) == "Do nothing"
        assert cryptocurrency_action(10) == "Do nothing"
        assert cryptocurrency_action(10.526315789473685) == "Do nothing"



