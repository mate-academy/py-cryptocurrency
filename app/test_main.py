import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exc_rate:
        yield mock_exc_rate


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        pytest.param(100, 90, "Sell all your cryptocurrency",
                     id="Should sell if prediction more than 5 percent lower"),
        pytest.param(100, 120, "Buy more cryptocurrency",
                     id="Should buy if prediction more than 5 percent higher"),
        pytest.param(100, 105, "Do nothing",
                     id="Should return 'Do nothing' if not much diff higher"),
        pytest.param(100, 95, "Do nothing",
                     id="Should return 'Do nothing' if not much diff lower")
    ]
)
def test_cryptocurrency_action_returns_correct_values(
        mocked_exchange: callable,
        current_rate: int | float,
        predicted_rate: int | float,
        expected: str
) -> None:
    mocked_exchange.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
