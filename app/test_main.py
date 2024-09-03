from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction_return,current_rate,expectation",
    [
        (0.6, 1, "Sell all your cryptocurrency"),
        (1.6, 1, "Buy more cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more(
        mocked_prediction: float,
        prediction_return: float | int,
        current_rate: float | int,
        expectation: str
) -> None:

    mocked_prediction.return_value = prediction_return
    assert cryptocurrency_action(1) == expectation
