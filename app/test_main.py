import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize("predicted_exchange, current, expected", [
    (106, 100, "Buy more cryptocurrency"),
    (93, 100, "Sell all your cryptocurrency"),
    (99, 100, "Do nothing"),
    (105, 100, "Do nothing"),
    (95, 100, "Do nothing")

])
def test_crypto_currency_action(
        predicted_exchange: Union[int, float],
        current: Union[int, float],
        expected: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_get_exchange_rate:
        mocked_get_exchange_rate.return_value = predicted_exchange
        result = cryptocurrency_action(current)
        assert result == expected
