from unittest import mock
import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyActionClass:
    @pytest.mark.parametrize(
        "current_rate, exchange_rate, result",
        [
            pytest.param(
                100, 95, "Do nothing",
                id="test nothing to do less than current rate"
            ),
            pytest.param(
                100, 105, "Do nothing",
                id="test nothing to do more than current rate"
            ),
            pytest.param(
                100, 120, "Buy more cryptocurrency",
                id="test to buy more cryptocurrency"
            ),
            pytest.param(
                100, 80, "Sell all your cryptocurrency",
                id="test to sell all your cryptocurrency"
            )
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_works(
            self,
            mocked_get_exchange_rate_prediction,
            current_rate,
            exchange_rate,
            result,

    ):
        mocked_get_exchange_rate_prediction.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == result
