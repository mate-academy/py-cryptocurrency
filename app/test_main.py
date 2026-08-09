import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch


@pytest.mark.parametrize(
    "current_rate, predict_rate, expected",
    [
        (100, 93, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 103, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 107, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(current_rate: int | float,
                               predict_rate: int | float,
                               expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predict_rate):
        assert cryptocurrency_action(current_rate) == expected
