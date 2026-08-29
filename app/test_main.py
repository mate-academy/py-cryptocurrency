import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1)
def test_if_called(mocked_get_exchange_rate: mock.Mock) -> None:
    cryptocurrency_action(1)
    mocked_get_exchange_rate.assert_called_once_with(1)


@pytest.mark.parametrize(
    "current_rate, prediction_rate, action",
    [
        pytest.param(
            1,
            1.00,
            "Do nothing",
            id="rate-unchanged"
        ),
        pytest.param(
            1,
            1.05,
            "Do nothing",
            id="buy-threshold"
        ),
        pytest.param(
            1,
            0.95,
            "Do nothing",
            id="sell-threshold"
        ),
        pytest.param(
            1,
            0.94,
            "Sell all your cryptocurrency",
            id="below-sell-threshold"
        ),
        pytest.param(
            1,
            1.06,
            "Buy more cryptocurrency",
            id="above-buy-threshold"
        ),

        pytest.param(
            67.67,
            71.05,
            "Do nothing",
            id="rate-near-buy-threshold"
        ),
        pytest.param(
            67.67,
            64.29,
            "Do nothing",
            id="rate-near-sell-threshold"
        ),
        pytest.param(
            67.67,
            64.28,
            "Sell all your cryptocurrency",
            id="rate-below-sell-threshold"
        ),
        pytest.param(
            67.67,
            71.06,
            "Buy more cryptocurrency",
            id="rate-above-buy-threshold"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate: mock.Mock,
        current_rate: int | float,
        prediction_rate: int,
        action: str
) -> None:
    mocked_get_exchange_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == action
