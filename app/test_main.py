import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (0.82, 1, "Sell all your cryptocurrency"),
        (1.75, 1, "Buy more cryptocurrency"),
        (1.03, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: mock,
                               prediction_rate: float,
                               current_rate: float,
                               expected_result: str) -> None:

    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
