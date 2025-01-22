import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_exchange_rate_is_more_than_5_percent_higher(
            self,
            mock_exchange: int | float
    ) -> None:
        mock_exchange.return_value = 1.06
        current_rate = 1
        self.assertEqual(
            cryptocurrency_action(current_rate), "Buy more cryptocurrency"
        )

    @patch("app.main.get_exchange_rate_prediction")
    def test_exchange_rate_is_more_than_5_percent_lower(
            self,
            mock_exchange: int | float
    ) -> None:
        mock_exchange.return_value = 0.94
        current_rate = 1.00
        self.assertEqual(
            cryptocurrency_action(current_rate), "Sell all your cryptocurrency"
        )


if __name__ == "__main__":
    unittest.main()
