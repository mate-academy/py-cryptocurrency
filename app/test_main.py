import pytest

from unittest import mock
from typing import Union, Any

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @mock.patch("app.main.get_exchange_rate_prediction")
    @pytest.mark.parametrize(
        "prediction_rate, "
        "result, "
        "current_rate", [
            pytest.param(
                2.1,
                "Do nothing",
                2,
                id="test prediction_rate / current_rate = 1.05"
            ),
            pytest.param(
                1.9,
                "Do nothing",
                2,
                id="test prediction_rate / current_rate = 0.95"
            ),
            pytest.param(
                2.0,
                "Do nothing",
                2,
                id="test prediction_rate / current_rate > 0.95"
            ),
            pytest.param(
                2.2,
                "Buy more cryptocurrency",
                2,
                id="test prediction_rate / current_rate > 1.05"
            ),
            pytest.param(
                1.8,
                "Sell all your cryptocurrency",
                2,
                id="test prediction_rate / current_rate < 0.95"
            )
        ]
    )
    def test_cryptocurrency_action(
            self,
            mock_rate_prediction: mock.Mock,
            prediction_rate: Union[int, float],
            result: str,
            current_rate: int
    ) -> None:

        mock_rate_prediction.return_value = prediction_rate

        assert cryptocurrency_action(current_rate) == result

    @pytest.mark.parametrize(
        "current_rate", [
            pytest.param(
                "1.8",
                id="test get 'string' should raising Type Error"
            ),
            pytest.param(
                {1.8},
                id="test get 'set' should raising Type Error"
            ),
            pytest.param(
                {1: 8},
                id="test get 'dict' should raising Type Error"
            ),
            pytest.param(
                [1, 8],
                id="test get 'list' should raising Type Error"
            ),
            pytest.param(
                (1, 8),
                id="test get 'tupl' should raising Type Error"
            )
        ]
    )
    def test_raising_errors_in_cryptocurrency_action(
            self,
            current_rate: Any,

    ) -> None:

        with pytest.raises(TypeError):
            cryptocurrency_action(current_rate)

    @pytest.mark.parametrize(
        "current_rate", [
            pytest.param(
                0,
                id="test division by 0 should raising ZeroDivisionError"
            ),
            pytest.param(
                0.0,
                id="test float division by 0 should raising ZeroDivisionError"
            )
        ]
    )
    def test_division_by_zero_in_cryptocurrency_action(
            self,
            current_rate: Any,

    ) -> None:

        with pytest.raises(ZeroDivisionError):
            cryptocurrency_action(current_rate)
