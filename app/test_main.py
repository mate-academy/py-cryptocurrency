import unittest
from unittest import mock
from parameterized import parameterized
import app.main


class TestCryptocurrencyAction(unittest.TestCase):

    @parameterized.expand([
        (100, 107, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 104.99, "Do nothing"),
        (100, 95.01, "Do nothing"),
        (3, 3.15, "Do nothing"),
        (1, 0.95, "Do nothing")
    ])
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self, current_rate: float,
                                   predicted_rate: None, expected_action: None,
                                   mock_get_exchange_rate_prediction:
                                   None) -> None:
        mock_get_exchange_rate_prediction.return_value = predicted_rate

        result = app.main.cryptocurrency_action(current_rate)
        self.assertEqual(result, expected_action)


if __name__ == "__main__":
    unittest.main()
