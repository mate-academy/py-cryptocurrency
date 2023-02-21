from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def get_exchange_rate_prediction():
    return mock.MagicMock()


def test_cryptocurrency_buy(get_exchange_rate_prediction) -> None:
    get_exchange_rate_prediction.return_value = 1.5
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_do_nothing(get_exchange_rate_prediction) -> None:
    get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(0.92) == "Do nothing"


def test_cryptocurrency_sell(get_exchange_rate_prediction) -> None:
    get_exchange_rate_prediction.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
