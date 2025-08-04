import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted, expected",
    [
        (106.0, "Buy more cryptocurrency"),
        (94.0, "Sell all your cryptocurrency"),
        (100.0, "Do nothing"),
        (105.0, "Do nothing"),
        (95.0, "Do nothing"),
        (104.9, "Do nothing"),
        (95.1, "Do nothing"),
    ]
)
def test_cryptocurrency_action(predicted: float, expected: str) -> None:
    curent: float = 100.0
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted
               ):
        result: str = cryptocurrency_action(curent)
        assert result == expected
