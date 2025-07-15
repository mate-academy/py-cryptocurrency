from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predict_rate, current_rate, result",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (0.93, 1, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_main(mocked_func, predict_rate, current_rate, result):
    mocked_func.return_value = predict_rate

    assert cryptocurrency_action(current_rate) == result
