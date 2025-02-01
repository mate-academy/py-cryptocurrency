from app.main import cryptocurrency_action
import unittest
from unittest import mock

class TestCryptocurrencyAction(unittest.TestCase):

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self, mock_prediction: mock.MagicMock) -> None:
        test_cases = [
            (100, 105.01, "Buy more cryptocurrency"),
            (100, 94.99, "Sell all your cryptocurrency"),
            (100, 105.0, "Do nothing"),
            (100, 95.0, "Do nothing"),
            (50, 52.51, "Buy more cryptocurrency"),
            (50, 47.49, "Sell all your cryptocurrency"),
            (50, 50, "Do nothing"),
        ]

        for current_rate, predicted_rate, expected in test_cases:
            mock_prediction.return_value = predicted_rate
            result = cryptocurrency_action(current_rate)
            self.assertEqual(result, expected)
