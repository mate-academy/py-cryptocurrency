from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mocked_rate, result",
    [
        (100, 20, "Sell all your cryptocurrency"),
        (2, 20, "Buy more cryptocurrency"),
        (20, 20, "Do nothing"),
        (20, 19, "Do nothing"),
        (20, 21, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        mocked_rate: int,
        result: str
) -> None:

    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        mocked.return_value = mocked_rate

        assert cryptocurrency_action(current_rate) == result
