import unittest
from unittest.mock import Mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    def setUp(self):
        self.mock_get_exchange_rate_prediction = Mock()

    def test_buy_more_cryptocurrency(self) -> None:
        self.mock_get_exchange_rate_prediction.return_value = 1.1

        action = cryptocurrency_action(1.0)

        self.assertEqual(action, "Buy more cryptocurrency")

    def test_sell_all_cryptocurrency(self) -> None:
        self.mock_get_exchange_rate_prediction.return_value = 0.9

        action = cryptocurrency_action(1.0)

        self.assertEqual(action, "Sell all your cryptocurrency")

    def test_do_nothing(self) -> None:
        self.mock_get_exchange_rate_prediction.return_value = 1.03

        action = cryptocurrency_action(1.0)

        self.assertEqual(action, "Do nothing")


if __name__ == "__main__":
    unittest.main()
