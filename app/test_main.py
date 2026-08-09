from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate,predicted_percentage,result",
    [
        (50, 1.12, "Buy more cryptocurrency"),
        (167.4, 0.88, "Sell all your cryptocurrency"),
        (20, 0.95, "Do nothing"),
        (79, 1.05, "Do nothing"),
        (101.95, 1.01, "Do nothing")

    ]
)
def test_cryptocurrency_action(
        exchange_rate: int | float, predicted_percentage: float, result: str
) -> None:
    with (mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = (
            exchange_rate * predicted_percentage
        )
        assert cryptocurrency_action(exchange_rate) == result
        mock_get_exchange_rate_prediction.assert_called_once_with(
            exchange_rate
        )
