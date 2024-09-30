import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_prediction_rate, current_rate, expected",
    [
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    mock_prediction_rate: float,
    current_rate: float,
    expected: str
) -> None:

    mock_get_exchange_rate_prediction.return_value = mock_prediction_rate
    assert cryptocurrency_action(current_rate) == expected
