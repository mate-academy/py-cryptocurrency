from typing import Callable
from unittest import mock, TestCase

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):
    def setUp(self) -> None:
        self.current_rate = 100

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self,
                                     mock_exchange_rate_prediction:
                                     Callable) -> None:
        mock_exchange_rate_prediction.return_value = self.current_rate * 1.1
        result = cryptocurrency_action(self.current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self,
                                     mock_exchange_rate_prediction:
                                     Callable) -> None:
        mock_exchange_rate_prediction.return_value = self.current_rate * 0.9
        result = cryptocurrency_action(self.current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self,
                        mock_exchange_rate_prediction:
                        Callable) -> None:
        mock_exchange_rate_prediction.return_value = self.current_rate * 1.02
        result = cryptocurrency_action(self.current_rate)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_not_sell_at_0_95(self,
                                 mock_exchange_rate_prediction:
                                 Callable) -> None:
        mock_exchange_rate_prediction.return_value = self.current_rate * 0.95
        result = cryptocurrency_action(self.current_rate)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_not_buy_at_1_05(self,
                                mock_exchange_rate_prediction:
                                Callable) -> None:
        mock_exchange_rate_prediction.return_value = self.current_rate * 1.05
        result = cryptocurrency_action(self.current_rate)
        self.assertEqual(result, "Do nothing")
