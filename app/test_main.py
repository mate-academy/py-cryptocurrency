import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: int
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 105
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: int
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 95
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self,
            mock_get_exchange_rate_prediction: int
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 100
        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")


if __name__ == "__main__":
    unittest.main()
