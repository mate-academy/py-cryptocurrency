import unittest
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    def test_buy_more_cryptocurrency(self):
        action = cryptocurrency_action(1000)
        self.assertEqual(action, "Buy more cryptocurrency")

    def test_sell_all_cryptocurrency(self):
        action = cryptocurrency_action(1000)
        self.assertEqual(action, "Sell all your cryptocurrency")

    def test_do_nothing(self):
        action = cryptocurrency_action(1000)
        self.assertEqual(action, "Do nothing")

    def test_edge_case_current_rate_zero(self):
        action = cryptocurrency_action(0)
        self.assertEqual(action, "Do nothing")


if __name__ == '__main__':
    unittest.main()
