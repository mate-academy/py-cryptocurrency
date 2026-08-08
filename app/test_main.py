from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCryptoCurrencyAction:
    @pytest.mark.parametrize(
        "current_rate, prediction_rate, expected",
        [
            pytest.param(
                1,
                1.1,
                "Buy more cryptocurrency",
                id="Buy more cryptocurrency"
            ),
            pytest.param(
                1,
                0.95,
                "Do nothing",
                id="Do nothing"
            ),
            pytest.param(
                1,
                1,
                "Do nothing",
                id="Do nothing"
            ),
            pytest.param(
                1,
                1.05,
                "Do nothing",
                id="Do nothing"
            ),
            pytest.param(
                1,
                0.9,
                "Sell all your cryptocurrency",
                id="Sell all your cryptocurrency"
            ),
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction: mock.Mock,
            current_rate: float or int,
            prediction_rate: float or int,
            expected: str
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected
