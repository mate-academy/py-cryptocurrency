from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked:
        yield mocked


def test_do_nothing(mocked_exchange_prediction: None) -> None:
    mocked_exchange_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_2(mocked_exchange_prediction: None) -> None:
    mocked_exchange_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_3(mocked_exchange_prediction: None) -> None:
    mocked_exchange_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_buy_more_cryptocurrency(mocked_exchange_prediction: None) -> None:
    mocked_exchange_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_your_cryptocurrency(mocked_exchange_prediction: None) -> None:
    mocked_exchange_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
