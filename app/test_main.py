from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def current_rate() -> int | float:
    return 1


@pytest.fixture()
def prediction_rate() -> int | float:
    return 3.5


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_call_get_exchange_rate_prediction(
        rate_prediction: mock,
        current_rate: int | float,
        prediction_rate: int | float
) -> None:
    rate_prediction.return_value = prediction_rate
    cryptocurrency_action(current_rate)
    rate_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "pred_rate, cur_rate, result",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (0.1, 10, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ],
)
def test_should_return_correct_prediction(
        rate_prediction: mock,
        pred_rate: int | float,
        cur_rate: int | float,
        result: str
) -> None:
    rate_prediction.return_value = pred_rate
    assert cryptocurrency_action(cur_rate) == result
