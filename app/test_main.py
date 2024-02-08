from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCryptoClass:
    @pytest.mark.parametrize(
        "current_rate,prediction_rate,message",
        [
            pytest.param(
                1,
                2,
                "Buy more cryptocurrency"
            ),
            pytest.param(
                1,
                0.1,
                "Sell all your cryptocurrency"
            ),
            pytest.param(
                1,
                0.95,
                "Do nothing"
            ),
            pytest.param(
                1,
                1.05,
                "Do nothing"
            ),
        ]
    )
    def test_(
            self,
            prediction_rate: int | float,
            current_rate: int | float,
            message: str,
    ) -> None:
        with (mock.patch("app.main.get_exchange_rate_prediction")
              as mocked_function):
            mocked_function.return_value = prediction_rate
            assert cryptocurrency_action(current_rate) == message
