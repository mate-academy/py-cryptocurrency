from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, result",
    [
        pytest.param(
            1.07,
            "Buy more cryptocurrency",
            id="if currency high need to buy more"
        ),
        pytest.param(
            0.9,
            "Sell all your cryptocurrency",
            id="if currency low need to sell more"
        ),
        pytest.param(1,
                     "Do nothing",
                     id="if currency not high and not low do nothing"),
        pytest.param(
            1.05,
            "Do nothing",
            id="if currency not high and not low do nothing"
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="if currency not high and not low do nothing"
        ),
    ],
)
def test_cryptocurrency_action_with_different_currency(
    current_rate: int | float, result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = current_rate
        assert cryptocurrency_action(1) == result
