from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, expected_result",
    [
        (0.95, 1.0, "Buy more cryptocurrency"),
        (0.90, 1.0, "Buy more cryptocurrency"),
        (1.05, 1.0, "Do nothing"),
        (0.96, 1.0, "Do nothing"),
        (1.01, 1.0, "Do nothing"),
        (1.00, 0.95, "Do nothing"),
        (1.00, 1.05, "Do nothing"),
        (1.16, 1.0, "Sell all your cryptocurrency"),
        (1.20, 1.0, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_function: object,
                               current_rate: int,
                               prediction: int,
                               expected_result: str) -> None:
    mock_function.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
