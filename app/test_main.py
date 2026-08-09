import unittest
from unittest.mock import patch, MagicMock


from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction", return_value=1.09)
    def test_buy_when_gt_5_percent_difference(
        self, mock_exchange_rate: MagicMock
    ) -> None:
        self.assertEqual(
            cryptocurrency_action(1), "Buy more cryptocurrency"
        )

    @patch("app.main.get_exchange_rate_prediction", return_value=0.92)
    def test_sell_when_gt_5_percent_difference(
        self, mock_exchange_rate: MagicMock
    ) -> None:
        self.assertEqual(
            cryptocurrency_action(1), "Sell all your cryptocurrency"
        )

    @patch("app.main.get_exchange_rate_prediction", return_value=0.99)
    def test_action_when_lt_5_percent_difference(
        self, mock_exchange_rate: MagicMock
    ) -> None:
        self.assertEqual(
            cryptocurrency_action(1), "Do nothing"
        )

    @patch("app.main.get_exchange_rate_prediction", return_value=0.95)
    def test_sell_at_boundary_value(
        self, mock_exchange_rate: MagicMock
    ) -> None:
        self.assertEqual(
            cryptocurrency_action(1), "Do nothing"
        )

    @patch("app.main.get_exchange_rate_prediction", return_value=1.05)
    def test_buy_at_boundary_value(
        self, mock_exchange_rate: MagicMock
    ) -> None:
        self.assertEqual(
            cryptocurrency_action(1), "Do nothing"
        )


if __name__ == "__main__":
    unittest.main()
