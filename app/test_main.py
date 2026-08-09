import pytest

from unittest. mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted, current, expected",
    [
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (105.01, 100, "Buy more cryptocurrency"),
        (94.99, 100, "Sell all your cryptocurrency"),
    ]
)
def test_cryptocurrency_action(predicted: float,
                               current: float,
                               expected: str) -> str:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predicted):
        assert cryptocurrency_action(current) == expected
