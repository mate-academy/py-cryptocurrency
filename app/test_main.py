import pytest
from unittest.mock import patch
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predict_rate,action,expected_result", [
        (1.07, 1, "Buy more cryptocurrency"),
        (0.91, 1, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_predict: Union[int, float],
        predict_rate: Union[int, float],
        action: Union[int, float],
        expected_result: str) -> None:
    mock_get_exchange_rate_predict.return_value = predict_rate
    assert cryptocurrency_action(action) == expected_result
