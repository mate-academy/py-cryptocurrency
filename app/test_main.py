from unittest.mock import patch, MagicMock
import pytest
from app.main import cryptocurrency_action


class TestCryptocurrency:
    @pytest.mark.parametrize(
         "prediction_rate, current_rate, result",
        [
            (100, 30, "Buy more cryptocurrency"),
            (10, 10, "Do nothing"),
            (25, 50, "Sell all your cryptocurrency")
        ]
    )
    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction,
            prediction_rate,
            current_rate,
            result
    ):
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        prediction = cryptocurrency_action(current_rate)
        assert prediction == result

