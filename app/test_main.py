import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("mock_prediction, expected", [
    (106.0, "Buy more cryptocurrency"),
    (94.0, "Sell all your cryptocurrency"),
    (100.5, "Do nothing"),
    (105.0, "Do nothing"),
    (95.0, "Do nothing")
])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        monk_get_exchange_rate_prediction: patch,
        mock_prediction: float,
        expected: str
) -> None:
    monk_get_exchange_rate_prediction.return_value = mock_prediction
    assert cryptocurrency_action(100) == expected
