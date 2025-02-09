import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import get_exchange_rate_prediction

@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (100, 105, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_exchange_rate: MagicMock,
    current_rate: int,
    predicted_rate: int,
    expected: str
) -> None:
    mock_exchange_rate.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
