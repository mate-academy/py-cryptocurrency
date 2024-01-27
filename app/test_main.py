from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (5, 6, "Buy more cryptocurrency"),
        (5, 4, "Sell all your cryptocurrency"),
        (5, 5.25, "Do nothing"),
        (5, 4.75, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate: int | float,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
