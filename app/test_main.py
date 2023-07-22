import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,result",
    [
        pytest.param(
            12,
            12.7,
            "Buy more cryptocurrency",
            id="Limit number for purchase"
        ),
        pytest.param(
            23,
            21.8,
            "Sell all your cryptocurrency",
            id="Limit number for sell"
        ),
        pytest.param(
            20,
            21,
            "Do nothing",
            id="Limit number for `do nothing`"
        ),
        pytest.param(
            40,
            38,
            "Do nothing",
            id="LImit number for 'do nothing'"
        )
    ]
)
def test_function_output_with_different_prediction_rate(
        current_rate: int | float,
        prediction: int | float,
        result: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = prediction
        assert (
            cryptocurrency_action(current_rate) == result
        )
