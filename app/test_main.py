import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "exchange_rate, current_rate, result",
    [
        (0.95, 0.95, "Do nothing"),
        (0.5, 0.2, "Sell all your cryptocurrency"),
        (0.2, 0.8, "Buy more cryptocurrency")
    ]
)
def test_cryptocurrency_action(exchange_rate: Union[int, float],
                               current_rate: Union[int, float],
                               result: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
            as mocked_get_exchange_rate_prediction):

        mocked_get_exchange_rate_prediction.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == result
