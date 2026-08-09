import unittest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


class TestCryptocurrency(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_lower_value_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction: MagicMock) -> None:
        mock_get_exchange_rate_prediction.return_value = 95

        result = cryptocurrency_action(100)

        expected = "Do nothing"

        self.assertEqual(result, expected)

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_upper_value_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction: MagicMock) -> None:
        mock_get_exchange_rate_prediction.return_value = 105

        result = cryptocurrency_action(100)

        expected = "Do nothing"

        self.assertEqual(result, expected)
