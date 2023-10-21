import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, result",
    [
        (1.05, 1.3, "Buy more cryptocurrency"),
        (1.06, 0.9, "Sell all your cryptocurrency"),
        (1.05, 1.04, "Do nothing"),
        (1.05, 1.03, "Do nothing")
    ],
)
def test_cryptocurrency_action(
        current_rate: float,
        prediction_rate: float,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        mocked_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
