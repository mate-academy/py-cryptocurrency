from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


class TestCryptocurrency:
    @pytest.mark.parametrize(
        "prediction_rate, current_rate, result",
        [
            (100, 30, "Buy more cryptocurrency"),
            (10, 10, "Do nothing"),
            (25, 50, "Sell all your cryptocurrency"),
            (9.5, 10, "Do nothing"),
            (10.5, 10, "Do nothing"),
        ]
    )
    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction: str,
            prediction_rate: int,
            current_rate: int,
            result: str
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        prediction = cryptocurrency_action(current_rate)
        assert prediction == result
