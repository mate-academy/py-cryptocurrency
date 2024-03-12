from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,result",
    [
        (1.3, "Buy more cryptocurrency"),
        (0.8, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock,
        prediction_rate: int | float,
        result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(1.0) == result
