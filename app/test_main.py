from unittest import mock

from app.main import (
    cryptocurrency_action
)


def test_return_buy_if_exchange_rate_is_more() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 106
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"


def test_return_sell_if_exchange_rate_is_less() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 94
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"


def test_return_buy_if_exchange_rate_more_than_5() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 105
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_return_sell_if_exchange_rate_less_than_5() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 95
        result = cryptocurrency_action(100)
        assert result == "Do nothing"


def test_return_nothing_if_difference_not_big() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = 101
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
