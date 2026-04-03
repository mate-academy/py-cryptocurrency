import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_rate",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 104.9, "Do nothing"),
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 95.1, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction,
    current_rate: float,
    predicted_rate: float,
    expected_rate: str
) -> None:
    mock_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)

    error_msg = (
        f"Ожидалось: '{expected_rate}', получено: '{result}' "
        f"Курс: {current_rate}, прогноз: {predicted_rate}"
    )

    assert result == expected_rate, error_msg
    mock_prediction.assert_called_once()
