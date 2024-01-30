from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "rate, expected_result",
    [
        (110, "Buy more cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
        (105, "Do nothing"),
        (95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        rate: int | float,
        expected_result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as rate_prediction):
        rate_prediction.return_value = rate
        assert cryptocurrency_action(100) == expected_result
