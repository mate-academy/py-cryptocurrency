from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, exchange_rate, result",
    [
        (5, 5.68, "Buy more cryptocurrency"),
        (5, 4.55, "Sell all your cryptocurrency"),
        (5, 5.25, "Do nothing"),
        (5, 4.75, "Do nothing"),
        (5, 5.12, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: int, exchange_rate: float, result: str
) -> None:
    with (
        mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=exchange_rate
        ),
    ):
        assert cryptocurrency_action(current_rate) == result
