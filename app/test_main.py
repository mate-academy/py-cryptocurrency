from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,rate_prediction, message",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing")
    ]
)
def test_return_right_message(current_rate, rate_prediction, message):
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_predict:
        mocked_predict.return_value = rate_prediction

        advise = cryptocurrency_action(current_rate)
        print(advise)
        assert advise == message


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_call_get_exchange_rate_prediction(mocked_rate_prediction):
    current_rate = 1
    mocked_rate_prediction.return_value = 1

    cryptocurrency_action(current_rate)

    mocked_rate_prediction.assert_called_once()
