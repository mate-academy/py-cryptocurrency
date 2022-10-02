from app.main import cryptocurrency_action

import pytest
from unittest import mock


@pytest.mark.parametrize(
    "value,expected_rezult",
    [
        (1575.03, "Buy more cryptocurrency"),
        (750.75, "Sell all your cryptocurrency"),
        (1032.95, "Do nothing"),
        (1050, "Do nothing"),
        (950, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction, value, expected_rezult):
    mock_prediction.return_value = value
    action = cryptocurrency_action(1000)
    assert action == expected_rezult
