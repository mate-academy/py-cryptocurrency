import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_try_to_take_diff_entrance(mock_rate_prediction: patch,
                                   current_rate: int,
                                   exchange_rate: float,
                                   expected: str) -> None:
    mock_rate_prediction.return_value = exchange_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
