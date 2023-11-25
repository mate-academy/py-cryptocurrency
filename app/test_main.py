import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: int | float
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.06

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: int | float
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.94

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self,
            mock_get_exchange_rate_prediction: int | float
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.03

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_105_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: int | float
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.05

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency",
                         "You should not buy cryptocurrency when"
                         " prediction_rate / current_rate == 1.05")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_95_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: int | float
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.95

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency",
                         "You should not sell cryptocurrency when"
                         " prediction_rate / current_rate == 0.95")


if __name__ == "__main__":
    unittest.main()
