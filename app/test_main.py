import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (5, 2, "Buy more cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (2, 5, "Sell all your cryptocurrency"),
        (0.95, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_exchange: mock,
                               prediction_rate: int | float,
                               current_rate: int | float,
                               expected_result: str) -> None:
    mock_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
