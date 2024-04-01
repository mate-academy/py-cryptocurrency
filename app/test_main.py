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
def test_exchange_rate(
        mock_get_exchange_rate_prediction: pytest.param,
        exchange_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result
