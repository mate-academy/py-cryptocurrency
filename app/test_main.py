import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,advice",
    [
        (1.0, 1.15, "Buy more cryptocurrency"),
        (1.0, 0.69, "Sell all your cryptocurrency"),
        (1.0, 1.01, "Do nothing"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_prediction(
    mocked_get_exchange_rate_prediction: mock,
    current_rate: int | float,
    prediction_rate: int | float,
    advice: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == advice
