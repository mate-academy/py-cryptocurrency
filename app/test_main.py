import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected",
    [
        (1.06, 1.00, "Buy more cryptocurrency"),  # +6% зростання
        (0.94, 1.00, "Sell all your cryptocurrency"),  # -6% падіння
        (1.05, 1.00, "Do nothing"),  # +4% зростання (менше 5%)
        (0.95, 1.00, "Do nothing"),  # -4% падіння (менше 5%)
        (1.00, 1.00, "Do nothing"),  # Без змін
    ],
)
@patch("app.main.get_exchange_rate_prediction", autospec=True)
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: float,
    predicted_rate: float,
    current_rate: float,
    expected: str,
) -> None:
    """Перевіряє правильність роботи cryptocurrency_action."""

    # Налаштовуємо мок-функцію
    mock_get_exchange_rate_prediction.return_value = predicted_rate

    # Викликаємо тестовану функцію
    result = cryptocurrency_action(current_rate)

    # Перевіряємо результат
    assert result == expected

    # Перевіряємо, що функція справді викликалася
    mock_get_exchange_rate_prediction.assert_called_once()
