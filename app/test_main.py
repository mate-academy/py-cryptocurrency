import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (1.0, 1.1, "Buy more cryptocurrency"),
        (1.0, 0.9, "Sell all your cryptocurrency"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing"),
        (1.0, 1.03, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_get_exchange_rate_prediction: float,
                               current_rate: float,
                               predicted_rate: float,
                               expected: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
