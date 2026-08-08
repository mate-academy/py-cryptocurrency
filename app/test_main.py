import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, action", [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction: mock,
                               current_rate: int | float,
                               predicted_rate: int | float,
                               action: str) -> None:
    mocked_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == action
