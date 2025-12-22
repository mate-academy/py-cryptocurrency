import unittest
from unittest.mock import Mock, patch

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_should_buy_when_prediction_is_significantly_higher(
        self,
        mock_predict: Mock,
    ) -> None:
        mock_predict.return_value = 110

        result = cryptocurrency_action(100)

        self.assertEqual(result, "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_should_sell_when_prediction_is_significantly_lower(
        self,
        mock_predict: Mock,
    ) -> None:
        mock_predict.return_value = 90

        result = cryptocurrency_action(100)

        self.assertEqual(result, "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_should_do_nothing_when_prediction_is_within_range(
        self,
        mock_predict: Mock,
    ) -> None:
        mock_predict.return_value = 102

        result = cryptocurrency_action(100)

        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_should_do_nothing_at_exactly_plus_five_percent(
        self,
        mock_predict: Mock,
    ) -> None:
        mock_predict.return_value = 105

        result = cryptocurrency_action(100)

        self.assertEqual(result, "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_should_do_nothing_at_exactly_minus_five_percent(
        self,
        mock_predict: Mock,
    ) -> None:
        mock_predict.return_value = 95

        result = cryptocurrency_action(100)

        self.assertEqual(result, "Do nothing")
