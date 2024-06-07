import pytest
from unittest import mock

from app.main import cryptocurrency_action

@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(100, 120, "Buy more cryptocurrency"),
        pytest.param(100, 80, "Sell all your cryptocurrency"),
        pytest.param(100, 105, "Do nothing"),
        pytest.param(100, 95, "Do nothing"),
        pytest.param(100, 98, "Do nothing")
        
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_rate: mock.Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    mocked_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
