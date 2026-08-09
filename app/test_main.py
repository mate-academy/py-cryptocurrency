from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        (100, 104, "Do nothing"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 110, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock.Mock,
        current_rate: int,
        prediction_rate: int,
        expected_result: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
