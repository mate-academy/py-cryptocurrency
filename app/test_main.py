from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as get_rate:
        yield get_rate


def test_buy_more_crypto(mocked_rate_prediction: mock) -> None:
    mocked_rate_prediction.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_your_crypto(mocked_rate_prediction: mock) -> None:
    mocked_rate_prediction.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_rate_prediction: mock) -> None:
    mocked_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"

    mocked_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
