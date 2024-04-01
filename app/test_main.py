import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate, current_rate, expected_result",
    [(82, 7, "Buy more cryptocurrency"),
     (1, 4, "Sell all your cryptocurrency"),
     (45, 46, "Do nothing"),
     (85, 85.6, "Do nothing")]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange(
        mock_get_exchange: pytest.param,
        exchange_rate: int,
        current_rate: int,
        expected_result: int
) -> None:
    mock_get_exchange.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result
