import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current, predicted, exspected",
    [
        (20, 23, "Buy more cryptocurrency"),
        (800, 759, "Sell all your cryptocurrency"),
        (50, 52.5, "Do nothing"),
        (50, 47.5, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: mock.Mock,
                               current: int | float,
                               predicted: int | float,
                               exspected: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted
    assert cryptocurrency_action(current) == exspected
