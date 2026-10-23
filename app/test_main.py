import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected",
    [
        (110, "Buy more cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
        (100, "Do nothing"),
        (105, "Do nothing"),
        (95, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_pred: MagicMock,
    predicted_rate: int,
    expected: str,
) -> None:
    mock_pred.return_value = predicted_rate

    result = cryptocurrency_action(100)

    assert result == expected
