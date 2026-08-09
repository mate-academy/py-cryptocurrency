import unittest
from unittest import mock
from app.main import cryptocurrency_action


class CryptocurrencyActionTestCase(unittest.TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_predicted_rate_within_range1(
            self,
            mock_prediction: float) -> None:
        mock_prediction.return_value = 0.94
        current_rate = 1.0
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_rate_105_percent_do_nothing3(
            self,
            mock_prediction: float) -> None:
        mock_prediction.return_value = 1.05
        current_rate = 1.0
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_rate_95_percent_do_nothing4(
            self,
            mock_prediction: float) -> None:
        mock_prediction.return_value = 0.95
        current_rate = 1.0
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_predicted_rate_within_range2(
            self,
            mock_prediction: float) -> None:
        mock_prediction.return_value = 1.06
        current_rate = 1.0
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")


if __name__ == "__main__":
    unittest.main()
