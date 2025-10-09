from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_result",
    [
        (100, 94, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(current_rate: float, predicted_rate: float,
                               expected_result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected_result
