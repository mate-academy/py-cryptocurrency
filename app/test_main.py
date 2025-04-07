import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self,
                                     mock_prediction:
                                     unittest.mock.Mock) -> None:
        mock_prediction.return_value = 105.1  # >5% increase from 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self,
                                     mock_prediction:
                                     unittest.mock.Mock) -> None:
        mock_prediction.return_value = 94.9  # >5% decrease from 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_upper_boundary(self,
                                       mock_prediction:
                                       unittest.mock.Mock) -> None:
        mock_prediction.return_value = 105.0  # exactly +5%
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_lower_boundary(self,
                                       mock_prediction:
                                       unittest.mock.Mock) -> None:
        mock_prediction.return_value = 95.0  # exactly -5%
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_middle_range(self,
                                     mock_prediction:
                                     unittest.mock.Mock) -> None:
        mock_prediction.return_value = 102  # <5% increase from 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

        mock_prediction.return_value = 97.1  # <5% decrease from 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")


if __name__ == "__main__":
    unittest.main()
