import unittest
from unittest.mock import patch
from typing import Union
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self, mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:  # noqa: E501
        current_rate: Union[int, float] = 100
        mock_get_exchange_rate_prediction.return_value = 106  # 6% higher
        self.assertEqual(cryptocurrency_action(current_rate), "Buy more cryptocurrency")  # noqa: E501

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self, mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:  # noqa: E501
        current_rate: Union[int, float] = 100
        mock_get_exchange_rate_prediction.return_value = 94  # 6% lower
        self.assertEqual(cryptocurrency_action(current_rate), "Sell all your cryptocurrency")  # noqa: E501

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self, mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:  # noqa: E501
        current_rate: Union[int, float] = 100
        mock_get_exchange_rate_prediction.return_value = 102  # 2% higher
        self.assertEqual(cryptocurrency_action(current_rate), "Do nothing")

        mock_get_exchange_rate_prediction.return_value = 98  # 2% lower
        self.assertEqual(cryptocurrency_action(current_rate), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_boundary(self, mock_get_exchange_rate_prediction: unittest.mock.Mock) -> None:  # noqa: E501
        current_rate: Union[int, float] = 100
        mock_get_exchange_rate_prediction.return_value = 105  # Exactly 5% higher  # noqa: E501
        self.assertEqual(cryptocurrency_action(current_rate), "Do nothing")

        mock_get_exchange_rate_prediction.return_value = 95  # Exactly 5% lower
        self.assertEqual(cryptocurrency_action(current_rate), "Do nothing")


if __name__ == "__main__":
    unittest.main()
