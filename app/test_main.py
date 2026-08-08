from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ]
)
def test_rate_main(current_rate: int | float,
                   predicted_rate: int | float,
                   expected_result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected_result
