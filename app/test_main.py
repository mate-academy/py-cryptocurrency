import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 106, "Buy more cryptocurrency"),  # Предсказанный курс на 6% выше
    (100, 94, "Sell all your cryptocurrency"),  # Предсказанный курс на 6% ниже
    (100, 105, "Do nothing"),  # Предсказанный курс на 5% выше
    (100, 95, "Do nothing"),  # Предсказанный курс на 5% ниже
    (100, 100, "Do nothing"),  # Курс не изменился
])
def test_cryptocurrency_action(
    current_rate: int,
    predicted_rate: int,
    expected_action: None
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate
    ):
        assert cryptocurrency_action(current_rate) == expected_action
