import pytest

from typing import (Any, Union)

from unittest.mock import patch

import app.main


@pytest.mark.parametrize(
    "exchange_rate_prediction, result",
    [
        (1.06, "Buy more cryptocurrency"),
        (1.05, "Do nothing"),
        (1.00, "Do nothing"),
        (1, "Do nothing"),
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_exchange_rate_prediction: Any,
                               exchange_rate_prediction: Union[int, float],
                               result: str) -> str:
    mock_exchange_rate_prediction.return_value = exchange_rate_prediction
    test_result = app.main.cryptocurrency_action(1.0)
    assert test_result == result
