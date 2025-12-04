from app.main import cryptocurrency_action
from unittest import mock
import pytest
from typing import Any


@pytest.fixture()
def mock_function() -> Any:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        yield mock_prediction


@pytest.mark.parametrize(
    "pred_rate, curr_rate, exp",
    [
        (110, 100, "Buy more cryptocurrency"),
        (105.1, 100, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
        (100, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94.9, 100, "Sell all your cryptocurrency"),
        (85, 100, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        mock_function: Any,
        pred_rate: int | float,
        curr_rate: int | float,
        exp: str) -> None:
    mock_function.return_value = pred_rate
    result = cryptocurrency_action(curr_rate)
    assert result == exp
