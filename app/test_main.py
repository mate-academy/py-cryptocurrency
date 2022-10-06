from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (1.5, 1, "Buy more cryptocurrency"),
        (0.5, 1, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_mock_cryptocurrency_action(mocked_cryptocurrency_action,
                                    current_rate,
                                    prediction_rate,
                                    result):
    mocked_cryptocurrency_action.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
