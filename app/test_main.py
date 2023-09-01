from unittest import mock

import pytest

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (1.07, 1.00, "Buy more cryptocurrency"),
        (1.0, 1.7, "Sell all your cryptocurrency"),
        (1.05, 1.00, "Do nothing"),
        (1.00, 1.05, "Do nothing"),
        (0.95, 1.00, "Do nothing"),
    ],
)
def test_cryptocurrency_all_actions(
    mocked_prediction: mock.MagicMock,
    prediction_rate: int | float,
    current_rate: int | float,
    expected_result: str,
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
