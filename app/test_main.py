import pytest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange, action",
    [
        pytest.param(
            50, 51, "Do nothing"
        ),
        pytest.param(
            100, 95, "Do nothing"
        ),
        pytest.param(
            100, 105, "Do nothing"
        ),
        pytest.param(
            50, 100, "Buy more cryptocurrency"
        ),
        pytest.param(
            50, 20, "Sell all your cryptocurrency"
        )
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate: MagicMock,
        current_rate: int | float,
        exchange: int | float,
        action: str
) -> None:
    mock_get_exchange_rate.return_value = exchange

    assert cryptocurrency_action(current_rate) == action
