from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (1, 2, "Buy more cryptocurrency"),
        (1, 0.5, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ],
    ids=[
        "If correlation > 5% should return 'Buy more cryptocurrency'",
        "If correlation < 5% should return 'Sell all your cryptocurrency'",
        "If rates are equal should return 'Do nothing'",
        "If correlation = 0.95 should return 'Do nothing'",
        "If correlation = 1.05 should return 'Do nothing'"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        exchange_rate_prediction: mock.MagicMock,
        prediction_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
