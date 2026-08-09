import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        # Предсказанный курс выше на 6%
        (100.0, 106.0, "Buy more cryptocurrency"),
        # Предсказанный курс ниже на 6%
        (100.0, 94.0, "Sell all your cryptocurrency"),
        # Предсказанный курс выше на 3%
        (100.0, 103.0, "Do nothing"),
        # Предсказанный курс ниже на 3%
        (100.0, 97.0, "Do nothing"),
        # Предсказанный курс выше на 5% (граничное условие)
        (100.0, 105.0, "Do nothing"),
        # Предсказанный курс ниже на 5% (граничное условие)
        (100.0, 95.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float, predicted_rate: float, expected_action: str
) -> None:
    """
    Тестирует функцию cryptocurrency_action с различными входными данными.

    :param current_rate: Текущий курс обмена.
    :param predicted_rate: Предсказанный курс обмена.
    :param expected_action: Ожидаемое действие.
    """
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=predicted_rate
    ):
        assert cryptocurrency_action(current_rate) == expected_action
