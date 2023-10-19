from unittest import TestCase, mock

import app.main
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):
    @staticmethod
    def func(arg: int | float) -> str:
        return cryptocurrency_action(arg)

    def test_returns_string(self) -> None:
        self.assertTrue(self.func(1), str)

    def test_difference_is_not_important(self) -> None:
        app.main.get_exchange_rate_prediction = mock.Mock(return_value=1.00)

        self.assertEqual(self.func(1), "Do nothing")

    def test_difference_is_higher(self) -> None:
        app.main.get_exchange_rate_prediction = mock.Mock(return_value=1.05)

        self.assertEqual(self.func(1), "Buy more cryptocurrency")

    def test_difference_is_lower(self) -> None:
        app.main.get_exchange_rate_prediction = mock.Mock(return_value=0.95)

        self.assertEqual(self.func(1), "Sell all your cryptocurrency")
