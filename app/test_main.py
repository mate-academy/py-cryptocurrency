import unittest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    @patch("app.main.get_exchange_rate_prediction", return_value=106)
    def test_should_buy_more_when_rate_increases_over_5_percent(
        self, mock_prediction: MagicMock
    ) -> None:
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Buy more cryptocurrency")
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction", return_value=94)
    def test_should_sell_all_when_rate_decreases_over_5_percent(
        self, mock_prediction: MagicMock
    ) -> None:
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Sell all your cryptocurrency")
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction", return_value=102)
    def test_should_do_nothing_when_rate_increase_within_5_percent(
        self, mock_prediction: MagicMock
    ) -> None:
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction", return_value=98)
    def test_should_do_nothing_when_rate_decrease_within_5_percent(
        self, mock_prediction: MagicMock
    ) -> None:
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction", return_value=105)
    def test_should_do_nothing_when_rate_increase_exactly_5_percent(
        self, mock_prediction: MagicMock
    ) -> None:
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction", return_value=95)
    def test_should_do_nothing_when_rate_decrease_exactly_5_percent(
        self, mock_prediction: MagicMock
    ) -> None:
        current_rate = 100
        result = cryptocurrency_action(current_rate)
        self.assertEqual(result, "Do nothing")
        mock_prediction.assert_called_once_with(current_rate)
