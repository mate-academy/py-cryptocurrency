import pytest
from unittest.mock import patch, MagicMock

# Імпорт функції для тестування
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 102, "Do nothing"),
        (100, 99.5, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction_func: MagicMock,
    current_rate: float,  # Поточний курс криптовалюти
    predicted_rate: float,  # Прогнозований курс криптовалюти
    expected_action: str  # Очікувана дія
) -> None:
    """
    Тестує функцію cryptocurrency_action на основі різних прогнозів курсу.
    """
    # Мокуємо повернення значення від функції get_exchange_rate_prediction
    mock_prediction_func.return_value = predicted_rate

    # Перевіряємо, що функція cryptocurrency_action повертає правильну дію
    assert cryptocurrency_action(current_rate) == expected_action
