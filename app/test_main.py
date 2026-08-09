import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, result",
    [
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (1, 1, "Do nothing"),
        (2, 1, "Buy more cryptocurrency"),
        (1, 2, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_function(
        mocked_exchange: None,
        prediction_rate: float,
        current_rate: float,
        result: str) -> None:
    mocked_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
