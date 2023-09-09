from unittest import TestCase
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptoCurrency(TestCase):
    def test_funct_value_if_exchange_rate_higher_current_rate(
        self
    ) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
            mock_rate.return_value = 1.051
            res = cryptocurrency_action(1)

            self.assertEqual(res, "Buy more cryptocurrency")

    def test_funct_value_if_exchange_rate_lower_current_rate(
        self
    ) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
            mock_rate.return_value = 0.949
            res = cryptocurrency_action(1)

            self.assertEqual(res, "Sell all your cryptocurrency")

    def test_funct_value_if_difference_not_much(
        self
    ) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
            mock_rate.return_value = 1
            res = cryptocurrency_action(1)

            self.assertEqual(res, "Do nothing")
