import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @pytest.mark.parametrize(
        "current_rate, predicted_rate, expected_action",
        [
            (1.00, 1.10, "Buy more cryptocurrency"),
            (1.00, 0.90, "Sell all your cryptocurrency"),
            (1.00, 1.02, "Do nothing"),
        ]
    )
    @patch('app.main.get_exchange_rate_prediction')
    def test_cryptocurrency_action(
            self,
            mock_get_prediction,
            current_rate: float,
            predicted_rate: float,
            expected_action: str
    ) -> None:
        mock_get_prediction.return_value = predicted_rate

        assert cryptocurrency_action(current_rate) == expected_action
