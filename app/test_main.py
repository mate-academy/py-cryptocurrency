import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, result",
    [
        (20, 27, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (50, 50, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 50, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy(
        mocked_get_exchange_rate_prediction: Union[int, float],
        current_rate: int,
        predicted_rate: int,
        result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == result
