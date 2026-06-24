import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected_action",
    [
        (110, "Buy more cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
        (103, "Do nothing"),
        (105, "Do nothing"),
        (95, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        predicted_rate: int,
        expected_action: int
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = predicted_rate
        assert cryptocurrency_action(100) == expected_action
