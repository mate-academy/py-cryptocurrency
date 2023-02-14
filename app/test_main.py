from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "return_value, current_rate, expected_result",
    [
        (5, 10, "Sell all your cryptocurrency"),
        (20, 10, "Buy more cryptocurrency"),
        (10, 10, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction, return_value,
                               current_rate, expected_result):
    mock_prediction.return_value = return_value
    assert cryptocurrency_action(current_rate) == expected_result
