from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected_value",
    [
        (120, 100.3, "Buy more cryptocurrency"),
        (102.5, 100, "Do nothing"),
        (100, 150, "Sell all your cryptocurrency"),
        (1, 0.9, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing")
    ],
    ids=[
        "Increase more than 5 percent. Buy!",
        "Change within 5 percent: Do nothing!",
        "Decrease more than 5 percent: Sell!",
        "Value increase: Buy",
        "Change within 5 percent: Do nothing!",
        "do nothing! equal to 0.95 percent",
        "do nothing! equal to 1.05 percent"

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocket_get_exchange_rate_prediction: mock.Mock,
        predicted_rate: int | float,
        current_rate: int | float,
        expected_value: str,

) -> None:
    mocket_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_value
    mocket_get_exchange_rate_prediction.assert_called_once_with(current_rate)
