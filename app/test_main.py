from unittest.mock import patch, MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate: float, predicted_rate: float, expected_action: str",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 104.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 105.0, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_can_exchange_rate_prediction(mock_get_exchange_rate: MagicMock,
                                      current_rate: float,
                                      exchange_rate: float,
                                      expected_action: str) -> None:
    mock_get_exchange_rate.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_action
