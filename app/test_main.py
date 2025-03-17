import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Any


@pytest.mark.parametrize(
    "mock_prediction, expected",
    [
        (94, "Sell all your cryptocurrency"),
        (106, "Buy more cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing"),
        (100, "Do nothing")
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: Any,
    mock_prediction: float,
    expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = mock_prediction
    assert cryptocurrency_action(100) == expected
