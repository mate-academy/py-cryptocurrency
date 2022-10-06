from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_predict() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        yield mock_predict


def test_buy_more_cryptocurrency(mocked_predict: None) -> None:
    mocked_predict.return_value = 5
    assert cryptocurrency_action(3) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(mocked_predict: None) -> None:
    mocked_predict.return_value = 2
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"


def test_do_not_buy_more(mocked_predict: None):
    mocked_predict.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_not_sell(mocked_predict: None):
    mocked_predict.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
