import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (2, 5, "Buy more cryptocurrency"),
        (3, 1, "Sell all your cryptocurrency"),
        (2, 2.03, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ],
    ids=[
        "Test should return 'Buy more cryptocurrency' "
        "when prediction rate > current rate",
        "Test should return 'Sell all your cryptocurrency' "
        "when prediction rate < current rate",
        "Test should return 'Do nothing' "
        "when difference is not that much",
        "You should not sell cryptocurrency when "
        "prediction_rate / current_rate == 0.95",
        "You should not buy cryptocurrency "
        "when prediction_rate / current_rate == 1.05"
    ]
)
def test_cryptocurrency_action(current_rate: int | float,
                               prediction_rate: int | float,
                               expected: str
                               ) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        result = cryptocurrency_action(current_rate)
        assert result == expected
