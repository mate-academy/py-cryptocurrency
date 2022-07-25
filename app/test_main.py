import unittest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action, get_exchange_rate_prediction


class TestGetExchangeRatePrediction(unittest.TestCase):

    @patch("app.main.random")
    def test_get_exchange_rate_prediction_increase(self, mock_ran):
        mock_choice = MagicMock()
        mock_choice.choice = "increase"
        mock_choice.random = 0.5
        mock_ran.choice.return_value = mock_choice.choice
        mock_ran.random.return_value = mock_choice.random
        assert get_exchange_rate_prediction(10) == 20.00

    @patch("app.main.random")
    def test_get_exchange_rate_prediction_decrease(self, mock_ran):
        mock_choice = MagicMock()
        mock_choice.choice = "decrease"
        mock_choice.random = 0.5
        mock_ran.choice.return_value = mock_choice.choice
        mock_ran.random.return_value = mock_choice.random
        assert get_exchange_rate_prediction(10) == 5.00


class TestCryptocurrencyAction(unittest.TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_bye_more(
            self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 5
        assert cryptocurrency_action(4) == "Buy more cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_sell(
            self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 5
        assert cryptocurrency_action(10) == "Sell all your cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_do_nothing(
            self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 5
        assert cryptocurrency_action(5.1) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_if_095(
            self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 4.75
        assert cryptocurrency_action(5) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_if_105(
            self, mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 5.25
        assert cryptocurrency_action(5) == "Do nothing"
