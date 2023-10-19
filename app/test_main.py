import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate,action",
    [
        (20, 23, "Buy more cryptocurrency"),
        (800, 759, "Sell all your cryptocurrency"),
        (50, 52.5, "Do nothing"),
        (50, 47.5, "Do nothing")
    ],
    ids=[
        "if predicted change is more then 5%",
        "if predicted change is less then 5%",
        "if difference is not that much",
        "if difference is not that much"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: mock.Mock,
                               current_rate: int | float,
                               predicted_rate: int | float,
                               action: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == action
