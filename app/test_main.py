import pytest

from unittest import mock
from unittest.mock import Mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, percent, expected", [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.04, "Do nothing"),
        (1, 0.96, "Do nothing"),
        (1, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_rate: Mock,
        current_rate: int | float,
        percent: int | float,
        expected: str
) -> None:
    mock_rate.return_value = percent
    assert cryptocurrency_action(current_rate) == expected
