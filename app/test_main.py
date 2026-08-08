from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "current, predicted, expected",
    [
        (40, 45, "Buy more cryptocurrency"),
        (1800, 1600, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mok_get_exchange_rate_prediction: mock.Mock,
                               current: int | float,
                               predicted: int | float,
                               expected: str) -> None:
    mok_get_exchange_rate_prediction.return_value = predicted
    assert cryptocurrency_action(current) == expected
