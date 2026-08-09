from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_result,message",
    [
        (0.79, "Sell all your cryptocurrency"),
        (1.34, "Buy more cryptocurrency"),
        (1.0, "Do nothing"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing")
    ]
)
def test_cryptocurrency_action(mock_result: float | int, message: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        mock_func.return_value = mock_result
        assert cryptocurrency_action(1) == message
