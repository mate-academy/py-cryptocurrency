from typing import Any
from unittest import TestCase, mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction: Any
    ) -> None:
        test_cases = [
            {
                "current_rate": 1,
                "prediction_rate": 1.06,
                "expected": "Buy more cryptocurrency",
            },
            {
                "current_rate": 1,
                "prediction_rate": 0.94,
                "expected": "Sell all your cryptocurrency",
            },
            {
                "current_rate": 1,
                "prediction_rate": 1,
                "expected": "Do nothing",
            },
        ]

        for case in test_cases:
            mock_get_exchange_rate_prediction.return_value = (
                case.get("prediction_rate")
            )
            self.assertEqual(
                cryptocurrency_action(case.get("current_rate")),
                case.get("expected")
            )
