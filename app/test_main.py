from typing import Union

import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (10.6, 10, "Buy more cryptocurrency"),
        (9.4, 10, "Sell all your cryptocurrency"),
        (10.5, 10, "Do nothing"),
        (9.5, 10, "Do nothing")
    ],
    ids=[
        "Should buy cryptocurrency if prediction_rate / current_rate > 1.05",
        "Should sell cryptocurrency if prediction_rate / current_rate < 0.95",
        "Should do nothing if prediction_rate / current_rate == 1.05",
        "Should do nothing if prediction_rate / current_rate == 0.95"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_buy_or_sell_cryptocurrency(
        mocked_rate_prediction: None,
        current_rate: Union[int, float],
        prediction_rate: float,
        result: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
