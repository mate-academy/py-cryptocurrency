from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,action",
    [
        [10, 15, "Buy more cryptocurrency"],
        [10, 5, "Sell all your cryptocurrency"],
        [10, 10.5, "Do nothing"],
        [10, 9.5, "Do nothing"],
        [10, 10, "Do nothing"]
    ],
    ids=[
        "You must buy more crypto, when coin GROWING is"
        "bigger or equal to 5%",
        "You must sell all you crypto, when coin FALLING is"
        "bigger or equal to 5%",
        "You must do NOTHING, when GROWING percent is lower then 5%",
        "You must do NOTHING, when FALLING percent is lower then 5%",
        "You must do NOTHING, when coin does not grow/fall"
    ]
)
def test_cryptocurrency_actions(
        current_rate: int | float,
        exchange_rate: int | float,
        action: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_exchange):
        mocked_exchange.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == action
