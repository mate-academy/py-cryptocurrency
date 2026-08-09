from unittest import mock
import pytest
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predict_value, current_value, expected_value",
    [
        pytest.param(
            3,
            2,
            "Buy more cryptocurrency",
            id="buy more if predicted rate more 5% higher than current rate"
        ),
        pytest.param(
            1,
            2,
            "Sell all your cryptocurrency",
            id="sell all if predicted rate is more 5% lower than current rate"
        ),
        pytest.param(
            2,
            2,
            "Do nothing",
            id="do nothing if difference is subtle"
        ),
        pytest.param(
            1.05,
            1,
            "Do nothing",
            id="do nothing if predicted rate is 5% higher than current rate"
        ),
        pytest.param(
            0.95,
            1,
            "Do nothing",
            id="do nothing if predicted rate is 5% lower than current rate"
        )
    ]
)
def test_cryptocurrency_action(
        predict_value: Union[int, float],
        current_value: Union[int, float],
        expected_value: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = predict_value

        assert cryptocurrency_action(current_value) == expected_value
