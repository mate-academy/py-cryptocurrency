import pytest
from app.main import cryptocurrency_action
from unittest.mock import MagicMock, patch


@pytest.mark.parametrize(
    "next_rate, current_rate, result",
    [
        (2, 1, "Buy more cryptocurrency"),
        (1.06, 1, "Buy more cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (0.94, 1, "Sell all your cryptocurrency"),
        (0.0, 1, "Sell all your cryptocurrency"),
        (2, 2, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_rate: MagicMock,
    next_rate: float,
    current_rate: float,
    result: str
) -> None:
    mock_rate.return_value = next_rate
    assert (
        cryptocurrency_action(current_rate) == result
    ), f"Expected {result} when next: {next_rate} and current: {current_rate}"
