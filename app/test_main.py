import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        yield mock_predict


def test_cryptocurrency_action_buy_more(mocked_prediction):
    mocked_prediction.return_value = 100
    assert cryptocurrency_action(0.94) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(mocked_prediction):
    mocked_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_buy_more_2(mocked_prediction):
    mocked_prediction.return_value = 21
    assert cryptocurrency_action(20) == "Do nothing"


def test_cryptocurrency_action_do_nothing(mocked_prediction):
    mocked_prediction.return_value = 19
    assert cryptocurrency_action(20) == "Do nothing"
