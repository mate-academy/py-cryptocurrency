from unittest.mock import Mock

import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("prediction_rate, current_rate, expected_result", [
    (100, 90, "Buy more cryptocurrency"),
    (110, 150, "Sell all your cryptocurrency"),
    (50, 50, "Do nothing"),
    (105, 100, "Do nothing"),
    (95, 100, "Do nothing")
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: Mock,
                               prediction_rate: float,
                               current_rate: float,
                               expected_result: str) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate

    result = cryptocurrency_action(current_rate)
    assert result == expected_result
