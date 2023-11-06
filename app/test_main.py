import pytest

from typing import Union

from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, message",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Union[int, float],
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        message: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    assert cryptocurrency_action(current_rate) == message
