import unittest
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_prediction: mock.Mock) -> None:
        mock_get_prediction.return_value = 106
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Buy more cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_your_cryptocurrency(
            self,
            mock_get_prediction: mock.Mock) -> None:
        mock_get_prediction.return_value = 94
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self,
            mock_get_prediction: mock.Mock) -> None:
        mock_get_prediction.return_value = 102
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_exactly_five_percent_buy(
            self,
            mock_get_prediction: mock.Mock) -> None:
        mock_get_prediction.return_value = 105
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_exactly_five_percent_sell(
            self,
            mock_get_prediction: mock.Mock) -> None:
        mock_get_prediction.return_value = 95
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")
