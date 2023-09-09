from typing import Union
from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction_rate, current_rate, result",
    [
        (1.051, 1, "Buy more cryptocurrency"),
        (0.949, 1, "Sell all your cryptocurrency"),
        (1.01, 1, "Do nothing"),
    ]
)
def test_cripto_currency(
    prediction_rate: Union[int | float],
    current_rate: Union[int | float],
    result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = prediction_rate

        assert cryptocurrency_action(current_rate) == result
