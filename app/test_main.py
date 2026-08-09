from typing import Any
from unittest import TestCase, mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
class TestCryptoCurrencyAction(TestCase):
    def test_if_exchange_rate_prediction_increased(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 10
        assert cryptocurrency_action(5) == "Buy more cryptocurrency"

    def test_boundry_exchange_rate_prediction_high(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 10.5
        assert cryptocurrency_action(10) == "Do nothing"

    def test_boundry_exchange_rate_prediction_low(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 4.75
        assert cryptocurrency_action(5) == "Do nothing"

    def test_if_exchange_rate_prediction_lowered(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 2
        assert cryptocurrency_action(5) == "Sell all your cryptocurrency"

    def test_if_exchange_rate_prediction_same(
            self, mock_get_exchange_rate_prediction: Any
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 5
        assert cryptocurrency_action(5) == "Do nothing"
