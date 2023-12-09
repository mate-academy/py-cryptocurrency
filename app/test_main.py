import pytest

from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, prediction_rate, expect_behavior",
    [
        (100.0, 120.0, "Buy more cryptocurrency"),
        (100.0, 50.0, "Sell all your cryptocurrency"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
    ],
    ids=[
        "exchange rate will increase by more than 1.05 - Buy",
        "exchange rate will decrease by more than 0.95 - Sell",
        "slight fluctuation of the exchange rate - Do nothing",
        "exchange rate equal 0.95 - Do nothing",
        "exchange rate equal 1.05 - Do nothing",
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock,
        current_rate: int | float,
        prediction_rate: int | float,
        expect_behavior: str) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expect_behavior
