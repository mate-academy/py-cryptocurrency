from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, result",
    [
        pytest.param(
            12, "Buy more cryptocurrency", id="predicted rate more 5%"
        ),
        pytest.param(
            9, "Sell all your cryptocurrency", id="predicted rate less 5%"
        ),
        pytest.param(
            10, "Do nothing", id="predicted rate equals current rate"
        ),
        pytest.param(
            10.5, "Do nothing", id="predicted rate is 5% higher"
        ),
        pytest.param(
            9.5, "Do nothing", id="predicted rate is 5% lower "
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_predicted_rate: mock.Mock,
    prediction_rate: int | float,
    result: str
) -> None:
    mocked_predicted_rate.return_value = prediction_rate
    assert cryptocurrency_action(10) == result
