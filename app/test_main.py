from unittest import mock
from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, result",
    [
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing"),
        (1.06, "Buy more cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_exchange_rate_more_105_percent(
        mock_get_exchange_rate_prediction: mock,
        exchange_rate: float,
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(1) == result
