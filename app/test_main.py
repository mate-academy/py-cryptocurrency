from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate_prediction,current_rate,action",
    [
        (104.99, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (105.01, 100, "Buy more cryptocurrency"),
        (95.01, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94.99, 100, "Sell all your cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
        exchange_rate_prediction: float | int,
        current_rate: float | int,
        action: str
) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_get_exchange_rate_prediction
    ):
        mock_get_exchange_rate_prediction.return_value = (
            exchange_rate_prediction
        )
        assert cryptocurrency_action(current_rate) == action
