import unittest
from typing import Union
from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
class TestCryptocurrencyAction(unittest.TestCase):

    def test_prediction_greater_then_current(
            self, prediction: Union[int, float]) -> None:
        current = 200.2
        prediction.return_value = 220.5
        assert cryptocurrency_action(current) == "Buy more cryptocurrency"

    def test_prediction_smaller_then_current(
            self, prediction: Union[int, float]) -> None:
        current = 200.7
        prediction.return_value = 157.3
        assert cryptocurrency_action(current) == "Sell all your cryptocurrency"

    def test_prediction_some_as_current(
            self, prediction: Union[int, float]) -> None:
        current = 200.7
        prediction.return_value = 199.9
        assert cryptocurrency_action(current) == "Do nothing"

    def test_prediction_greater_at_five_percent(
            self, prediction: Union[int, float]) -> None:
        current = 100
        prediction.return_value = 105
        assert cryptocurrency_action(current) == "Do nothing"

    def test_prediction_smaller_at_five_percent(
            self, prediction: Union[int, float]) -> None:
        current = 200
        prediction.return_value = 190
        assert cryptocurrency_action(current) == "Do nothing"
