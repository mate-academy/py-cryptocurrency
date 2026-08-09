from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current_rate, expected_value",
    [
        (110, 100.2, "Buy more cryptocurrency"),
        (104.9, 100, "Do nothing"),
        (90, 100, "Sell all your cryptocurrency"),
        (1, 0.9, "Buy more cryptocurrency"),
        (200, 205, "Do nothing"),
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing")
    ],
    ids=[
        "Increase more than 5 percent: Buy",
        "Change within 5 percent: Do nothing",
        "Decrease more than 5 percent: Sell",
        "Tiny value increase: Buy",
        "Small change, within 5 percent: Do nothing",
        "do nothing when equal to 0.95 percent",
        "do nothing when equal to 1.05 percent"

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocket_get_exchange_rate_prediction: mock.Mock,
        prediction: int | float,
        current_rate: int | float,
        expected_value: str,

) -> None:
    mocket_get_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_value
    mocket_get_exchange_rate_prediction.assert_called_once_with(current_rate)
