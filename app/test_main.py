from unittest import mock
from app import main
import pytest


@pytest.mark.parametrize(
    "current_rate,prediction_rate,action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock.Mock,
        current_rate: float,
        prediction_rate: float,
        action: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction_rate
    result = main.cryptocurrency_action(current_rate)
    assert result == action
