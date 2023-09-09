from typing import Union
from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction_rate, current_rate, result",
    [
        (10.51, 10, "Buy more cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.949, 1, "Sell all your cryptocurrency"),
        (0.95, 1, "Do nothing"),
        (20, 20, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cripto_currency(
    mock_rate: mock.Mock,
    prediction_rate: Union[int | float],
    current_rate: Union[int | float],
    result: str
) -> None:
    mock_rate.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == result
