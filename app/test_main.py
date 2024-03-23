from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("exchange_rate, expected_action", [
    (115.0, "Buy more cryptocurrency"),
    (85.0, "Sell all your cryptocurrency"),
    (100.0, "Do nothing"),
    (95.0, "Do nothing"),
    (105.0, "Do nothing"),
])
def test_cryptocurrency_action(
        exchange_rate: int | float, expected_action: int | float
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=exchange_rate
    ):
        assert cryptocurrency_action(100) == expected_action
