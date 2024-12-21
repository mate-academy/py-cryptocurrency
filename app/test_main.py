import unittest
from unittest.mock import patch, Mock
from app.main import get_exchange_rate_prediction, cryptocurrency_action


class TestCryptocurrencyFunction(unittest.TestCase):
    @patch("random.choice")
    @patch("random.random")
    def test_get_exchange_rate_prediction_increase(
            self,
            mock_random: Mock,
            mock_choice: Mock
    ) -> None:
        mock_random.return_value = "increase"
        mock_choice.return_value = 0.5

        exchange_rate = 100
        result = get_exchange_rate_prediction(exchange_rate)

        self.assertEqual(result, round(exchange_rate / 0.5, 2))

    @patch("random.choice")
    @patch("random.random")
    def test_get_exchange_rate_prediction_decrease(
            self,
            mock_random: Mock,
            mock_choice: Mock
    ) -> None:
        mock_random.return_value = "decrease"
        mock_choice.return_value = 0.5

        exchange_rate = 100
        result = get_exchange_rate_prediction(exchange_rate)

        self.assertEqual(result, round(exchange_rate * 0.5, 2))

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_buy(
            self,
            mock_prediction: Mock
    ) -> None:
        mock_prediction.return_value = 110

        current_rate = 100
        result = cryptocurrency_action(current_rate)

        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_sell(
            self,
            mock_prediction: Mock
    ) -> None:
        mock_prediction.return_value = 90

        current_rate = 100
        result = cryptocurrency_action(current_rate)

        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_do_nothing(self, mock_prediction: Mock) -> None:
        mock_prediction.return_value = 102

        current_rate = 100
        result = cryptocurrency_action(current_rate)

        self.assertEqual(result, "Do nothing")


if __name__ == "__main__":
    unittest.main()
