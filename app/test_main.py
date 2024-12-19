from unittest import mock
import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, exchange_rate, answer",
    [
        (5, 5.25, "Do nothing"),
        (5, 4.75, "Do nothing"),
    ]
)
def test_check_correct_result(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: int | float,
        exchange_rate: int | float,
        answer: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == answer
