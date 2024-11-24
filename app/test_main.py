import pytest
from typing import Any

import app
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "init_current_rate, second_rate, expected_result",
    [
        pytest.param(1,
                     2,
                     "Buy more cryptocurrency",
                     id="Predicted exchange rate "
                        "is more than 5% higher"),
        pytest.param(1,
                     0.5,
                     "Sell all your cryptocurrency",
                     id="Predicted exchange "
                        "is more than 5% lower"),
        pytest.param(1,
                     1,
                     "Do nothing",
                     id="Difference is not too big"),
        pytest.param(1,
                     1.05,
                     "Do nothing",
                     id="Rate equal 1.05"),
        pytest.param(1,
                     0.95,
                     "Do nothing",
                     id="Rate equal 0.95")
    ]
)
def test_cryptocurrency_action(monkeypatch: Any,
                               init_current_rate: int,
                               second_rate: int,
                               expected_result: str) -> None:
    def mock_get_exchange_rate_prediction(init_rate: int) -> int:
        return second_rate

    monkeypatch.setattr(app.main,
                        "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    result = cryptocurrency_action(init_current_rate)
    assert result == expected_result
