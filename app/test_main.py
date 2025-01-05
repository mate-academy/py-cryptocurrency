import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptoCurrencyAction:
    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self, mock_get_rate):
        test_cases = [
            (105, "Do nothing"),
            (110, "Buy more cryptocurrency"),
            (95, "Do nothing"),
            (90, "Sell all your cryptocurrency"),
        ]

        for predicted_rate, expected_result in test_cases:
            mock_get_rate.return_value = predicted_rate
            result = cryptocurrency_action(100)
            assert result == expected_result

pytest.main()