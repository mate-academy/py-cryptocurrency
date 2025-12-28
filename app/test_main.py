import pytest
from unittest import mock

from app.main import cryptocurrency_action

rate = 255


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (rate, rate * 1.06, "Buy more cryptocurrency"),
        (rate, rate * 1.05, "Do nothing"),
        (rate, rate * 0.95, "Do nothing"),
        (rate, rate * 0.94, "Sell all your cryptocurrency")
    ],
    ids=[
        "coeff 1.06 so buy more cryptocurrency",
        "coeff 1.05 so do nothing",
        "coeff 0.95 so do nothing",
        "coeff 0.94 so sell all cryptocurrency",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_rate: mock.MagicMock,
        current_rate: int | float,
        predicted_rate: int | float,
        expected: str) -> None:
    get_rate.return_value = predicted_rate
    res = cryptocurrency_action(current_rate)
    get_rate.assert_called_once()
    assert res == expected
