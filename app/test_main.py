from typing import Callable
import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "mocked_value, message",
        [
            (
                1.6,
                "Buy more cryptocurrency",
            ),
            (
                0.92,
                "Sell all your cryptocurrency"
            ),
            (
                1.05,
                "Do nothing"
            ),
            (
                0.95,
                "Do nothing"
            )
        ]
    )
    def test_crypto_currency_action(
            self,
            mocked_value: float,
            message: str,
            mocked_get_exchange_rate_prediction: Callable
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = mocked_value
        assert cryptocurrency_action(1) == message


def test_function_called(
        mocked_get_exchange_rate_prediction: Callable
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.01
    cryptocurrency_action(1)
    mocked_get_exchange_rate_prediction.assert_called_once_with(1)
