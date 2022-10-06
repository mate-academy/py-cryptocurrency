from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        yield mocked


def test_buy_more_crypto(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 9
    assert cryptocurrency_action(4) == "Buy more cryptocurrency"


def test_sell_all_crypto(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_not_buy(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_not_sell(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
