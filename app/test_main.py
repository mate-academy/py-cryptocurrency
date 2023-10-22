import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ]
)
def test_cryptocurrency_action(mocked_prediction: mock,
                               current_rate: int | float,
                               prediction_rate: int | float,
                               expected: str) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
