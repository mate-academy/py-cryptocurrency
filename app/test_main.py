import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, predict_rate, action",
    [
        pytest.param(
            100,
            200,
            "Buy more cryptocurrency",
            id="checking when rate more 1.05"
        ),
        pytest.param(
            200,
            100,
            "Sell all your cryptocurrency",
            id="checking when rate less 0.95"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="checking when rate equal 1"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="checking when rate equal around 1"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_future_move_with_currency(
    mocked_rate_prediction: callable,
    current_rate: float,
    predict_rate: float,
    action: str
) -> None:
    mocked_rate_prediction.return_value = predict_rate
    assert cryptocurrency_action(current_rate) == action
