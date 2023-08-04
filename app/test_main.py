from typing import Union
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (1.06, 1.00, "Buy more cryptocurrency"),
        (1.00, 1.06, "Sell all your cryptocurrency"),
        (1.05, 1.00, "Do nothing"),
        (1.00, 1.05, "Do nothing"),
        (0.95, 1.00, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result

# def test_cryptocurrency_action(mock_get_exchange_rate_prediction) -> None:
#     # Test case 1: Predicted rate is 10% higher
#     current_rate = 100  # Current exchange rate
#     predicted_rate = 110  # Predicted exchange rate (10% higher)
#     mock_get_exchange_rate_prediction.return_value = predicted_rate
#     assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
#
#     # Test case 2: Predicted rate is 10% lower
#     current_rate = 100  # Current exchange rate
#     predicted_rate = 90  # Predicted exchange rate (10% lower)
#     mock_get_exchange_rate_prediction.return_value = predicted_rate
#     assert cryptocurrency_action(current_rate) ==
#     "Sell all your cryptocurrency"
#
#     # Test case 3: Predicted rate is only 4% higher
#     current_rate = 100  # Current exchange rate
#     predicted_rate = 104  # Predicted exchange rate (4% higher)
#     mock_get_exchange_rate_prediction.return_value = predicted_rate
#     assert cryptocurrency_action(current_rate) == "Do nothing"
#
#     # Test case 4: Predicted rate is only 4% lower
#     current_rate = 100  # Current exchange rate
#     predicted_rate = 96  # Predicted exchange rate (4% lower)
#     mock_get_exchange_rate_prediction.return_value = predicted_rate
#     assert cryptocurrency_action(current_rate) == "Do nothing"
