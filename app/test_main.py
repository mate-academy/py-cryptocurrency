from unittest import TestCase
from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_when_increase(
        self, mock_prediction: Mock
    ) -> None:
        mock_prediction.return_value = 105.01
        result = cryptocurrency_action(100.0)
        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_when_decrease(
        self, mock_prediction: Mock
    ) -> None:
        mock_prediction.return_value = 94.99
        result = cryptocurrency_action(100.0)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_when_prediction_stable(
        self, mock_prediction: Mock
    ) -> None:

        for predicted in [95.0, 105.0, 100.0, 102.0]:
            mock_prediction.return_value = predicted
            result = cryptocurrency_action(100.0)
            self.assertEqual(result, "Do nothing")
