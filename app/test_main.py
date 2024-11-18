import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 100, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: patch,
    current_rate: float,
    predicted_rate: float,
    expected: str
) -> None:
    # Mocking the return value of get_exchange_rate_prediction
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)
    assert result == expected, (
        f"Помилка при перевірці current_rate={current_rate}, "
        f"predicted_rate={predicted_rate}, отримано {result}"
    )
