import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "exchange_rate, result",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing"),
    ]
)
def test_cryptocurrency_action(exchange_rate: Union[int, float],
                               result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction"
                    ) as mocked_exchange_rate:
        mocked_exchange_rate.return_value = exchange_rate
        assert cryptocurrency_action(100) == result
