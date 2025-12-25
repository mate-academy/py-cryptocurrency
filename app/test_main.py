from unittest import mock
from unittest.mock import Mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, result",
    [
        (6, "Buy more cryptocurrency"),
        (5 * 1.05, "Do nothing"),
        (5, "Do nothing"),
        (5 * 0.95, "Do nothing"),
        (4, "Sell all your cryptocurrency"),
    ],
    ids=[
        'should return "Buy more cryptocurrency"',
        'should return "Do nothing", when limit value',
        'should return "Do nothing"',
        'should return "Do nothing", when limit value',
        'should return "Sell all your cryptocurrency"'
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_has_called(
        mocked_get_prediction: Mock,
        prediction_rate: int,
        result: str
) -> None:
    cur_rate = 5
    mocked_get_prediction.return_value = prediction_rate
    assert cryptocurrency_action(cur_rate) == result
    mocked_get_prediction.assert_called_once_with(cur_rate)
