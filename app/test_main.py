from unittest import TestCase

from unittest.mock import patch

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):
    @patch("app.main.get_exchange_rate_prediction")
    def test_but_more_crypto(self, mock_prediction: int) -> None:
        mock_prediction.return_value = 110
        self.assertEqual(cryptocurrency_action(100), "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_crypto(self, mock_prediction: int) -> None:
        mock_prediction.return_value = 90
        self.assertEqual(cryptocurrency_action(100),
                         "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self, make_prediction: int) -> None:
        make_prediction.return_value = 104
        self.assertEqual(cryptocurrency_action(100), "Do nothing")
