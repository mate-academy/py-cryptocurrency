from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_prediction:
        yield mock_prediction


def test_should_return_buy_more(mocked_prediction):
    mocked_prediction.return_value = 6
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_should_return_sell_all(mocked_prediction):
    mocked_prediction.return_value = 4
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


def test_should_return_do_nothing(mocked_prediction):
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing2(mocked_prediction):
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
