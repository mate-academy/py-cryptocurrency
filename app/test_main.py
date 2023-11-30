import pytest
from unittest.mock import patch
from typing import Any

import app.main as main


@pytest.mark.parametrize(
    "exchange_rate, expected_result",
    [
        (1.06 * 100, "Buy more cryptocurrency"),
        (1.05 * 100, "Do nothing"),
        (100, "Do nothing"),
        (0.95 * 100, "Do nothing"),
        (0.94 * 100, "Sell all your cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_rate_prediction: Any,
        exchange_rate: float,
        expected_result: str
) -> None:
    main.get_exchange_rate_prediction = mock_exchange_rate_prediction

    mock_exchange_rate_prediction.return_value = exchange_rate
    result = main.cryptocurrency_action(100)
    assert result == expected_result
