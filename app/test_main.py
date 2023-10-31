from app.main import cryptocurrency_action

from unittest.mock import patch


@patch(
    "app.main.get_exchange_rate_prediction",
    return_value=0.95
)
def test_should_return_buy_more_cryptocurrency(
get_exchange_rate_prediction_mock: callable
) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@patch(
    "app.main.get_exchange_rate_prediction",
    return_value=1.05
)
def test_should_return_sell_cryptocurrency(
get_exchange_rate_prediction_mock: callable
) -> None:
    assert cryptocurrency_action(1) == "Do nothing"
