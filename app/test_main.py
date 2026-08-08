import unittest
from typing import Any
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_crypto_currency(
            self,
            mocked_get_exchange_rate_prediction: Any
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 1.06 * 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Buy more cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_crypto_currency(
            self,
            mocked_get_exchange_rate_prediction: Any
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 0.94 * 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_95_procent_do_nothing(
            self,
            mocked_get_exchange_rate_prediction: Any
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 0.95 * 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_105_procent_do_nothing(
            self,
            mocked_get_exchange_rate_prediction: Any
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 1.05 * 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")
