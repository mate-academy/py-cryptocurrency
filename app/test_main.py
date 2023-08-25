from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 106, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate: mock,
        current_rate: int,
        prediction_rate: int,
        expected_result: int,
) -> None:
    mock_get_exchange_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
