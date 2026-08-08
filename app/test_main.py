import unittest
from typing import Union
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.cryptocurrency_action")
    def test_buy_more_cryptocurrency(self,
                                     mock_get_exchange_rate_prediction:
                                     Union[int, float]) -> None:
        mock_get_exchange_rate_prediction.return_value = 105.06
        current_rate = 100.0
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self,
                                     mock_get_exchange_rate_prediction:
                                     Union[int, float]) -> None:
        mock_get_exchange_rate_prediction.return_value = 94.94
        current_rate = 100.0
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self,
                        mock_get_exchange_rate_prediction:
                        Union[int, float]) -> None:
        mock_get_exchange_rate_prediction.return_value = 101
        current_rate = 100.0
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")


if __name__ == "__main__":
    unittest.main()
