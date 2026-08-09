import pytest
from typing import Union
from unittest.mock import patch
import app.main as main


@pytest.mark.parametrize(
    "current, predicted, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 104.99, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 102, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current: Union[int, float],
    predicted: Union[int, float],
    expected: str,
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted):
        result = main.cryptocurrency_action(current)
    assert result == expected
