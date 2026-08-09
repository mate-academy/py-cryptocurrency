from unittest.mock import MagicMock, patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (105.1, 100, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
        (94.9, 100, "Sell all your cryptocurrency"),
        (95, 100, "Do nothing"),
        (100, 100, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: MagicMock,
    current_rate: int | float,
    prediction_rate: int | float,
    expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected_result
