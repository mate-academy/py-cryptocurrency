import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current,predicted,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
def test_get_correct(
        current: int,
        predicted: int,
        expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = predicted

        result = cryptocurrency_action(current)

    assert result == expected
