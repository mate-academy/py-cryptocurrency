from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCryptoAction:
    @pytest.mark.parametrize(
        "prediction_rate, result",
        [
            (1.06, "Buy more cryptocurrency"),
            (1.05, "Do nothing"),
            (0.9499, "Sell all your cryptocurrency"),
            (0.95, "Do nothing")
        ]
    )
    def test_cryptocurrency_action(
            self,
            prediction_rate: int | float,
            result: str,
    ) -> None:

        with mock.patch(
                "app.main.get_exchange_rate_prediction",
                return_value=prediction_rate
        ):
            assert cryptocurrency_action(1) == result
