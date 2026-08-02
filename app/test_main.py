from unittest.mock import MagicMock, patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_action",
    [
        (10.6, 10.0, "Buy more cryptocurrency"),
        (10.51, 10.0, "Buy more cryptocurrency"),
        (10.5, 10.0, "Do nothing"),
        (10.0, 10.0, "Do nothing"),
        (9.5, 10.0, "Do nothing"),
        (9.49, 10.0, "Sell all your cryptocurrency"),
        (9.4, 10.0, "Sell all your cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: MagicMock,
    prediction_rate: float,
    current_rate: float,
    expected_action: str,
) -> None:
    mock_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_action
