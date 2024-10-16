from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        pytest.param(100, 106,
                     "Sell all your cryptocurrency",
                     id="exchange rate is more than 5%"),
        pytest.param(100, 94,
                     "Buy more cryptocurrency",
                     id="exchange rate is more than 5% "
                        "lower from the current"),
        pytest.param(100, 102,
                     "Do nothing",
                     id="if difference is not that much"),
        pytest.param(100, 102,
                     "Do nothing",
                     id="difference not enough")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: mock,
    current_rate: float,
    predicted_rate: float,
    expected_action: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    action = cryptocurrency_action(current_rate)
    assert action == expected_action
