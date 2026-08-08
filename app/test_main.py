from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected",
    [
        pytest.param(1.0, 1.06, "Buy more cryptocurrency"),
        pytest.param(1.0, 0.94, "Sell all your cryptocurrency"),
        pytest.param(1.0, 0.95, "Do nothing"),
        pytest.param(1.0, 1.04, "Do nothing"),
        pytest.param(1.0, 1.05, "Do nothing"),
    ]
)
def test_exchange_rate(current_rate: int | float,
                       exchange_rate: float,
                       expected: str
                       ) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=exchange_rate):
        assert cryptocurrency_action(current_rate) == expected
