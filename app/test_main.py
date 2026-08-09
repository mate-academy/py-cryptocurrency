from unittest import mock
import pytest
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction,current,action",
    [
        (10.6, 10, "Buy more cryptocurrency"),
        (9.4, 10, "Sell all your cryptocurrency"),
        (10, 10, "Do nothing"),
        (10.5, 10, "Do nothing"),
        (9.5, 10, "Do nothing"),
    ]
)
def test_cryptocurrency_action_buy(mocked_get_exchange_rate_prediction: mock,
                                   prediction: int | float,
                                   current: int, action: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction
    result = cryptocurrency_action(current)
    mocked_get_exchange_rate_prediction.called_once()
    assert result == action
