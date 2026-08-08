from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, expected_rate, message",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_check_input_values(
        mocked_prediction: (int, float),
        current_rate: (int, float),
        expected_rate: (int, float),
        message: str
) -> None:
    mocked_prediction.return_value = expected_rate

    assert cryptocurrency_action(current_rate) == message
