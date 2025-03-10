import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),  # Курс увеличится на 6%
        (100, 94, "Sell all your cryptocurrency"),  # Курс уменьшится на 6%
        (100, 104, "Do nothing"),  # Курс увеличится на 4%
        (100, 96, "Do nothing"),  # Курс уменьшится на 4%
        (100, 95, "Do nothing"),  # Ровно 95% - не продаём
    ],
)
def test_cryptocurrency_action(
    current_rate: int,
    predicted_rate: float,
    expected_action: str,
) -> None:
    """
    Тестирует функцию cryptocurrency_action на различных сценариях.

    :param current_rate: Текущий курс криптовалюты.
    :param predicted_rate: Прогнозируемый курс криптовалюты.
    :param expected_action: Ожидаемое действие.
    """
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        assert cryptocurrency_action(current_rate) == expected_action
