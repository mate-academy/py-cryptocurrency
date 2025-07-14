from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency")
    ],
    ids=[
        "currency will remain unchanged",
        "currency will remain unchanged",
        "currency will grow up",
        "currency will fall down",
    ]
)
def test_cryptocurrency_action(prediction_rate: int | float,
                               current_rate: int | float,
                               result: str) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction") as mocked_func
    ):

        mocked_func.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
