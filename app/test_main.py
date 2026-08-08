from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


def test_action_buy_on_increase() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_rate_prediction):
        mock_rate_prediction.return_value = 110
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_action_sell_on_decrease() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_rate_prediction):
        mock_rate_prediction.return_value = 90
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "mock_value, rate_value",
    [
        (100, 100),
        (105, 100),
        (95, 100)
    ]
)
def test_no_action_on_small_change_with_boundary_value(
        mock_value: int | float,
        rate_value: int | float
) -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_rate_prediction):
        mock_rate_prediction.return_value = mock_value
        assert cryptocurrency_action(rate_value) == "Do nothing"
