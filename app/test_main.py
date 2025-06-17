import pytest
from unittest import mock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @pytest.mark.parametrize("rate_value, expected_value", [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.0, "Do nothing"),
        (1, "Do nothing")
    ])
    def test_cryptocurrency_action(
            self,
            rate_value: int | float,
            expected_value: str,
    ) -> None:
        with mock.patch("get_exchange_rate_prediction",
                        return_value=expected_value):

            res = cryptocurrency_action(rate_value)
            assert res == expected_value
