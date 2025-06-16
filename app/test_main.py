from unittest.mock import MagicMock

import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 104.9, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_prediction(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: int,
        exchange_rate: int,
        expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected
