from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (2.3, 2.1, "Buy more cryptocurrency"),
        (2.3, 2.5, "Sell all your cryptocurrency"),
        (2.3, 2.35, "Do nothing"),
        (1.05, 1.00, "Do nothing"),
        (0.95, 1.00, "Do nothing")
    ]
)
def test_cryptocurrency_action(mocked_prediction: int | float,
                               prediction_rate: int | float,
                               current_rate: int | float,
                               expected_result: str) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
