from unittest.mock import patch, MagicMock
import pytest
from typing import Union

import app.main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ],
    ids=[
        "high exchange rate - Buy",
        "low exchange rate - Sell",
        "1.05 exchange rate - Do nothing",
        "0.95 exchange rate - Do nothing"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_exchange_rate: MagicMock,
                               current_rate: Union[int, float],
                               predicted_rate: Union[int, float],
                               expected_result: str) -> None:
    mocked_exchange_rate.return_value = predicted_rate
    assert app.main.cryptocurrency_action(current_rate) == expected_result
