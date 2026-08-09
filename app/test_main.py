from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "get_exchange, expected_result", [
        (21.4, "Buy more cryptocurrency"),
        (2.01, "Sell all your cryptocurrency"),
        (5.0, "Do nothing"),
        (5.25, "Do nothing"),
        (4.75, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange: Mock,
        get_exchange: int | float,
        expected_result: str
) -> None:
    mock_get_exchange.return_value = get_exchange
    current_rate = 5
    assert cryptocurrency_action(current_rate) == expected_result
    mock_get_exchange.assert_called_once_with(current_rate)
