import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predict_rate,result",
    [
        (15, 20, "Buy more cryptocurrency"),
        (15, 14, "Sell all your cryptocurrency"),
        (15, 15, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_with_cryptocurrency(
        mocked_func,
        current_rate,
        predict_rate,
        result
):
    mocked_func.return_value = predict_rate
    assert cryptocurrency_action(current_rate) == result
