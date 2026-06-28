from typing import Union
from unittest.mock import Mock, patch

import pytest

import app.main as main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [

        (100, 106, "Buy more cryptocurrency"),
        (100, 105.01, "Buy more cryptocurrency"),
        (200, 211, "Buy more cryptocurrency"),
        (50, 53, "Buy more cryptocurrency"),


        (100, 94, "Sell all your cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (200, 189, "Sell all your cryptocurrency"),
        (50, 47, "Sell all your cryptocurrency"),


        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (200, 210, "Do nothing"),
        (200, 190, "Do nothing"),
        (100, 102, "Do nothing"),
        (100, 98, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: Mock,
    current_rate: Union[int, float],
    predicted_rate: Union[int, float],
    expected: str,
) -> None:
    mock_prediction.return_value = predicted_rate
    assert main.cryptocurrency_action(current_rate) == expected
