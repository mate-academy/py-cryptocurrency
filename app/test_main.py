import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "cur_rate, predict_rate, expected",
    [
        (0.5, 0.5, "Do nothing"),
        (1, 1, "Do nothing"),
        (0.2, 0.19, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (0.4, 0.7, "Buy more cryptocurrency"),
        (0.25, 0.6, "Buy more cryptocurrency"),
        (0.8, 0.3, "Sell all your cryptocurrency"),
        (0.3, 0.26, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_different_param(
        mocked_prediction: mock.Mock, cur_rate: int | float,
        predict_rate: int | float, expected: str) -> None:
    mocked_prediction.return_value = predict_rate
    assert cryptocurrency_action(cur_rate) == expected
