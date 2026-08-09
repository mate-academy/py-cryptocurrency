import unittest
from unittest import mock
from app.main import cryptocurrency_action


class CryptoTest(unittest.TestCase):
    def test_current_rate_buy(self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction",
                return_value=1.06
        ):
            result = cryptocurrency_action(1)
            self.assertEqual(result, "Buy more cryptocurrency")

    def test_current_rate_sell(self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction",
                return_value=0.94
        ):
            result = cryptocurrency_action(1)
            self.assertEqual(result, "Sell all your cryptocurrency")

    def test_current_rate_nothing(self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction",
                return_value=1
        ):
            result = cryptocurrency_action(1)
            self.assertEqual(result, "Do nothing")

    def test_current_rate_bound_1_05(self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction",
                return_value=1.05
        ):
            result = cryptocurrency_action(1)
            self.assertEqual(result, "Do nothing")

    def test_current_rate_bound_0_95(self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction",
                return_value=0.95
        ):
            result = cryptocurrency_action(1)
            self.assertEqual(result, "Do nothing")
