# write your code here
import unittest
from unittest import mock
from app.main import cryptocurrency_action


class TestMain(unittest.TestCase):

    def test_buy_more_crypto(self) -> None:
        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=106,
        ):
            result = cryptocurrency_action(100)
            self.assertEqual(result, "Buy more cryptocurrency")

    def test_sell_all_crypto(self) -> None:
        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=94,
        ):
            result = cryptocurrency_action(100)
            self.assertEqual(result, "Sell all your cryptocurrency")

    def test_do_nothing(self) -> None:

        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=100,
        ):
            result = cryptocurrency_action(100)
            self.assertEqual(result, "Do nothing")

    # Neue Testfälle für den Grenzfall: ratio == 1.05 und ratio == 0.95
    def test_do_nothing_at_upper_boundary(self) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction",
                        return_value=105):
            result = cryptocurrency_action(100)
            self.assertEqual(result, "Do nothing")

    def test_do_nothing_at_lower_boundary(self) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction",
                        return_value=95):
            result = cryptocurrency_action(100)
            self.assertEqual(result, "Do nothing")
