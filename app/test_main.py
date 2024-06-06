import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected", [
    (100, 105, "Buy more cryptocurrency"),
    (100, 95, "Sell all your cryptocurrency"),
    (100, 104, "Do nothing"),
    (100, 96, "Do nothing"),
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction, current_rate, predicted_rate, expected):
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
