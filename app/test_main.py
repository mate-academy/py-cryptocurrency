from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.fixture()
def mocked_exchange_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        yield mocked_prediction
        

def test_do_nothing(mocked_exchange_rate_prediction):
    mocked_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_buy_more_cryptocurrency(mocked_exchange_rate_prediction):
    mocked_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(mocked_exchange_rate_prediction):
    mocked_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_should_not_sell_cryptocurrency(mocked_exchange_rate_prediction):
    mocked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_not_buy_cryptocurrency(mocked_exchange_rate_prediction):
    mocked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"

# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_do_nothing(mocked_rate):
#     mocked_rate.return_value = 1
#     assert cryptocurrency_action(1) == "Do nothing"
# 
# 
# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_buy_more_cryptocurrency(mocked_rate):
#     mocked_rate.return_value = 1.06
#     assert cryptocurrency_action(1) == "Buy more cryptocurrency"
# 
# 
# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_sell_all_cryptocurrency(mocked_rate):
#     mocked_rate.return_value = 0.94
#     assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
# 
# 
# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_should_not_sell_cryptocurrency(mocked_rate):
#     mocked_rate.return_value = 0.95
#     assert cryptocurrency_action(1) == "Do nothing"
# 
# 
# @mock.patch("app.main.get_exchange_rate_prediction")
# def test_should_not_buy_cryptocurrency(mocked_rate):
#     mocked_rate.return_value = 1.05
#     assert cryptocurrency_action(1) == "Do nothing"
