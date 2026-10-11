from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, expected",
    [
        (110.12, "Buy more cryptocurrency"),
        (82.03, "Sell all your cryptocurrency"),
        (103.11, "Do nothing"),
        (94.99, "Sell all your cryptocurrency"),
        (95.01, "Do nothing"),
        (105.03, "Buy more cryptocurrency"),
        (95.00, "Do nothing"),
        (105.00, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction:
                               mock.MagicMock,
                               exchange_rate: float,
                               expected: str) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(100) == expected
