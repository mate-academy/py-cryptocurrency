from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,expected_result",
    [
        (1, 1.05, "Do nothing"),
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        exchange_rate_prediction: mock.MagicMock,
        current_rate: (int, float),
        exchange_rate: (int, float),
        expected_result: str
) -> None:
    exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result
    exchange_rate_prediction.assert_called_once()
