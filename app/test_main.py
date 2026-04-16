import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action
from unittest.mock import MagicMock


class TestCryptoAction(unittest.TestCase):
    def setUp(self) -> None:
        self.current_rate = 1000.0

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more(self, mock_prediction: MagicMock) -> None:
        mock_prediction.return_value = self.current_rate * 1.0501
        result = cryptocurrency_action(self.current_rate)
        mock_prediction.assert_called_once_with(self.current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all(self, mock_prediction: MagicMock) -> None:
        mock_prediction.return_value = self.current_rate * 0.9499
        result = cryptocurrency_action(self.current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_within_range(self, mock_prediction: MagicMock) -> None:
        mock_prediction.return_value = self.current_rate * 1.05
        self.assertEqual(
            cryptocurrency_action(self.current_rate),
            "Do nothing"
        )

        mock_prediction.return_value = self.current_rate * 0.95
        self.assertEqual(
            cryptocurrency_action(self.current_rate),
            "Do nothing"
        )

        mock_prediction.return_value = self.current_rate
        self.assertEqual(
            cryptocurrency_action(self.current_rate),
            "Do nothing"
        )


if __name__ == "__main__":
    unittest.main()
