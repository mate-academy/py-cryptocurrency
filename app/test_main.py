import pytest
from unittest import mock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "prediction_rate, current_rate, text",
        [
            pytest.param(
                1.06,
                100,
                "Buy more cryptocurrency",
                id="Cryptocurrency action with prediction_rate = 1.06"
            ),
            pytest.param(
                0.94,
                100,
                "Sell all your cryptocurrency",
                id="Cryptocurrency action with prediction_rate = 0.94"
            ),
            pytest.param(
                0.95,
                100,
                "Do nothing",
                id="Cryptocurrency action with prediction_rate = 0.95"
            ),
            pytest.param(
                1.05,
                100,
                "Do nothing",
                id="Cryptocurrency action with prediction_rate = 1.05"
            ),
        ]
    )
    def test_is_isogram(
            self,
            prediction_rate: float,
            current_rate: int,
            text: str
    ) -> None:
        with (mock.patch("app.main.get_exchange_rate_prediction")
              as mock_get_prediction):
            mock_get_prediction.return_value = prediction_rate * current_rate
            result = cryptocurrency_action(current_rate)
            assert result == text
