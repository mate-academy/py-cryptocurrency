import pytest
from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction, current, expected",
    [
        (105.1, 100.0, "Buy more cryptocurrency"),  # >5%
        (94.9, 100.0, "Sell all your cryptocurrency"),  # >5% down
        (104.9, 100.0, "Do nothing"),  # <5% up
        (95.1, 100.0, "Do nothing"),   # <5% down
        (105.0, 100.0, "Do nothing"),  # exactly 5% up
        (95.0, 100.0, "Do nothing"),   # exactly 5% down
    ],
)
def test_cryptocurrency_action(
    mock_prediction: MagicMock,
    prediction: float,
    current: float,
    expected: str,
) -> None:
    """
    Test cryptocurrency_action with mocked get_exchange_rate_prediction.
    """
    mock_prediction.return_value = prediction
    result = cryptocurrency_action(current)
    assert result == expected
