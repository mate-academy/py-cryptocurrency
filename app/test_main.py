import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [(4, 5, "Buy more cryptocurrency"),
     (10, 8, "Sell all your cryptocurrency"),
     (7, 7, "Do nothing"),
     (10, 9.5, "Do nothing"),
     (11, 11.55, "Do nothing")]
)
def test_get_exchange_rate_prediction(
        current_rate: int | float,
        predicted_rate: int | float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected
