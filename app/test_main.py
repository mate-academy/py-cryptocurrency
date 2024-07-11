from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mock_exchange_rate_return, expected_action",
    [
        (800, 1000, "Buy more cryptocurrency"),
        (1200, 1000, "Sell all your cryptocurrency"),
        (1000, 1000, "Do nothing"),
        (1000, 1050, "Do nothing"),
        (1000, 950, "Do nothing"),
    ],
    ids=[
        "Should return 'Buy more cryptocurrency' if coefficient > 1.05",
        "Should return 'Sell all your cryptocurrency' if coefficient < 0.95",
        "Should return 'Do nothing' if 1.05 > coefficient > 0.95",
        "Should return 'Do nothing' if coefficient == 1.05",
        "Should return 'Do nothing' coefficient == 0.95",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate(
        mock_get_exchange_rate_prediction: Mock,
        current_rate: int | float,
        mock_exchange_rate_return: int | float,
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = mock_exchange_rate_return
    assert cryptocurrency_action(current_rate) == expected_action
