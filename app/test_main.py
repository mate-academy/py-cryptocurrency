import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action
from unittest.mock import MagicMock


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected_result",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 100.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    current_rate: int,
    exchange_rate: float,
    expected_result: str
) -> None:

    mock_get_exchange_rate_prediction.return_value = exchange_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
