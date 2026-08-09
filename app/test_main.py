from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, current_rate, result",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.94, 1, "Sell all your cryptocurrency"),
        (0.95, 1, "Do nothing"),
        (1, 1, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        predicted_rate: float,
        current_rate: float,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        mocked.return_value = predicted_rate
        mocked_result = cryptocurrency_action(current_rate)
        assert mocked_result == result
