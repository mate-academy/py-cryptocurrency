from unittest import mock
import app.main
import unittest


class TestCryptocurrencyAction(unittest.TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self, mock_exchange_rate: float) -> None:
        mock_exchange_rate.return_value = 1.06
        result = app.main.cryptocurrency_action(1.0)
        self.assertEqual(result, "Buy more cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self, mock_exchange_rate: float) -> None:
        mock_exchange_rate.return_value = 0.94
        result = app.main.cryptocurrency_action(1.0)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self, mock_exchange_rate: float) -> None:
        mock_exchange_rate.return_value = 1.02
        result = app.main.cryptocurrency_action(1.0)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency_at_5_percent(
            self,
            mock_exchange_rate: float) -> None:
        mock_exchange_rate.return_value = 1.05
        result = app.main.cryptocurrency_action(1.0)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_when_rate_equal_95(self,
                                           mock_exchange_rate: float) -> None:
        mock_exchange_rate.return_value = 0.95
        result = app.main.cryptocurrency_action(1.0)
        self.assertEqual(result, "Do nothing")
