import pytest
from unittest import mock
from typing import Callable, Union


from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, prediction",
    [
        pytest.param(
            5, 5.55, "Buy more cryptocurrency",
            id="Should return Buy more cryptocurrency \
                when predicted rate is more than 5% higher from the current"
        ),
        pytest.param(
            10, 8.45, "Sell all your cryptocurrency",
            id="Should return Sell all your cryptocurrency \
                when predicted rate is more than 5% lower from the current"
        ),
        pytest.param(
            100, 100.2, "Do nothing",
            id="Should return Do nothing \
                when predicted rate is less than 5% higher from the current"
        ),
        pytest.param(
            70, 68.5, "Do nothing",
            id="Should return Do nothing \
                when predicted rate is less than 5% lower from the current"
        ),
        pytest.param(
            1, 1.05, "Do nothing",
            id="Should return Do nothing \
                when predicted rate is 5% higher from the current"
        ),
        pytest.param(
            1, 0.95, "Do nothing",
            id="Should return Do nothing \
                when predicted rate is 5% lower from the current"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_predict_correctly(
    mocked_rate: Callable,
    current_rate: Union[int, float],
    exchange_rate: Union[int, float],
    prediction: str
) -> None:
    mocked_rate.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == prediction
