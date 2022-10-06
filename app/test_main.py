import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,expected",
    [
        pytest.param(1, 1.06, "Buy more cryptocurrency",
                     id="Buy more cryptocurrency if rising more than 5%"),
        pytest.param(1, 0.94, "Sell all your cryptocurrency",
                     id="Sell all if falling more than 5%"),
        pytest.param(1, 1.05, "Do nothing",
                     id="Do nothing if rising less than 5%"),
        pytest.param(1, 0.95, "Do nothing",
                     id="Do nothing if falling less than 5%")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_rate(
        mocked_prediction,
        current_rate,
        prediction,
        expected
):
    mocked_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected
