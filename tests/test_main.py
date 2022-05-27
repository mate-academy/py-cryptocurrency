from app.main import cryptocurrency_action
from unittest import mock
import pytest


@mock.patch('app.main.get_exchange_rate_prediction')
class TestCryptocurrencyAction:

    def test_cryptocurrency_action_return_buy_more(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 150
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    def test_cryptocurrency_action_return_sell_all(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 80
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

    def test_cryptocurrency_action_return_do_nothing(self, mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = 100
        assert cryptocurrency_action(100 / 0.95) == "Do nothing"
        assert cryptocurrency_action(100 / 1.05) == "Do nothing"





