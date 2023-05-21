from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
    (100, 200, "Buy more cryptocurrency"),
    (100, 50, "Sell all your cryptocurrency"),
    (100, 95, "Do nothing"),
    (100, 105, "Do nothing")
])
def test_function_should_return_sell_all_your_cryptocurrency(
        current_rate: int,
        predicted_rate: int,
        expected_action: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        mocked_func.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == expected_action
