import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Callable


class TestCryptocurrencyPrediction:
    @pytest.mark.parametrize(
        "prediction_rate,current_rate,expected_result",
        [
            pytest.param(
                106.0,
                100.0,
                "Buy more cryptocurrency",
                id="should buy more"
            ),
            pytest.param(
                94.0,
                100.0,
                "Sell all your cryptocurrency",
                id="should sell all"
            ),
            pytest.param(
                95.0,
                100.0,
                "Do nothing",
                id="should do nothing"
            ),
            pytest.param(
                105.0,
                100.0,
                "Do nothing",
                id="should do nothing"
            )
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_rate_prediction: Callable,
            prediction_rate: float,
            current_rate: float,
            expected_result: str,
    ) -> None:
        mock_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
