from unittest.mock import patch
from typing import Union

from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with (
        (patch(
            "app.main.get_exchange_rate_prediction",
            return_value=15
        ))
    ):
        assert (
            cryptocurrency_action(Union[10])
            == "Buy more cryptocurrency"
        )


def test_sell_all() -> None:
    with (
        patch(
            "app.main.get_exchange_rate_prediction",
            return_value=5
        )
    ):
        assert (
            cryptocurrency_action(Union[10])
            == "Sell all your cryptocurrency"
        )


def test_do_nothing_if_0_95() -> None:
    with (
        (patch(
            "app.main.get_exchange_rate_prediction",
            return_value=9.5
        ))
    ):
        assert (
            cryptocurrency_action(Union[10])
            == "Do nothing"
        )


def test_do_nothing_if_1_05() -> None:
    with (
        (patch(
            "app.main.get_exchange_rate_prediction",
            return_value=10.5
        ))
    ):
        assert (
            cryptocurrency_action(Union[10])
            == "Do nothing"
        )
