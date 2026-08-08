import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,expected_value",
    [
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 106, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: int,
        exchange_rate: int,
        expected_value: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_value
