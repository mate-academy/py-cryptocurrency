from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_price,predicted_price,expected_action",
    [
        (100, 100 * 1.06, "Buy more cryptocurrency"),
        (200, 200 * 1.05, "Do nothing"),
        (12.5, 12.5 * 0.95, "Do nothing"),
        (75, 75 * 0.94, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_rate_prediction: mock.MagicMock,
        current_price: int | float,
        predicted_price: int | float,
        expected_action: str
) -> None:
    mock_exchange_rate_prediction.return_value = predicted_price
    assert cryptocurrency_action(current_price) == expected_action
