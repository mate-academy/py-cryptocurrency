import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        # сценарий Buy >5%
        (100, 106, "Buy more cryptocurrency"),
        # сценарий Sell >5%
        (100, 94, "Sell all your cryptocurrency"),
        # Do nothing <5%
        (100, 103, "Do nothing"),
        # границы +5%
        (100, 105, "Do nothing"),
        # границы -5%
        (100, 95, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float, predicted_rate: float, expected_result: str
) -> None:
    """
    Проверка всех сценариев cryptocurrency_action.
    Мокируем get_exchange_rate_prediction, чтобы тесты были предсказуемы.
    """
    with patch("app.main.get_exchange_rate_prediction", return_value=predicted_rate):
        result = cryptocurrency_action(current_rate)

    assert result == expected_result
