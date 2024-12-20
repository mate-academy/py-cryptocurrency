import unittest.mock
from unittest import TestCase
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCanPredictExchangeAction(TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_correct_buy_more_action(
            self,
            mock_exchange_rate: unittest.mock.MagicMock
    ) -> None:
        mock_exchange_rate.return_value = 1
        result = cryptocurrency_action(0.5)

        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_correct_dont_buy_more_if_equal_105_action(
            self,
            mock_exchange_rate: unittest.mock.MagicMock
    ) -> None:
        mock_exchange_rate.return_value = 1.05
        result = cryptocurrency_action(1)

        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_correct_dont_buy_more_if_equal_095_action(
            self,
            mock_exchange_rate: unittest.mock.MagicMock
    ) -> None:
        mock_exchange_rate.return_value = 0.95
        result = cryptocurrency_action(1)

        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_correct_sell_all_action(
            self,
            mock_exchange_rate: unittest.mock.MagicMock
    ) -> None:
        mock_exchange_rate.return_value = 1
        result = cryptocurrency_action(2)

        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_correct_do_nothing_action(
            self,
            mock_exchange_rate: unittest.mock.MagicMock
    ) -> None:
        mock_exchange_rate.return_value = 1
        result = cryptocurrency_action(1)

        self.assertEqual(result, "Do nothing")
