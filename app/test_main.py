from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
    ids=["buy", "sell"],
)
def test_cryptocurrency_action(
        current_rate: int,
        prediction_rate: int,
        expected_action: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as prediction:
        prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_action
