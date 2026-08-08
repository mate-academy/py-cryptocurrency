from typing import Any
from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, action",
    [
        pytest.param(100, 106, "Buy more cryptocurrency", id="> 5%"),
        pytest.param(100, 94, "Sell all your cryptocurrency", id="< 5%"),
        pytest.param(100, 105, "Do nothing", id="+- 5%"),
        pytest.param(100, 95, "Do nothing", id="+- 5%")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_main(mock_get_exchange_rate_prediction: Any,
              exchange_rate: int | float,
              current_rate: int | float,
              action: str) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate

    result = cryptocurrency_action(current_rate)
    assert result == action
