import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,expected",
    [
        pytest.param(1, 1.07, "Buy more cryptocurrency"),
        pytest.param(1, 0.90, "Sell all your cryptocurrency"),
        pytest.param(1, 1.05, "Do nothing"),
        pytest.param(1, 0.95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_rate(
        mocked_prediction, current_rate,
        prediction, expected
):
    mocked_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected
