import pytest
from unittest import mock
from app.main import cryptocurrency_action
from unittest.mock import MagicMock


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_test_random:
        yield mock_test_random


def test_buy_more(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_get_exchange_rate_prediction: MagicMock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.01
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_lower(mocked_get_exchange_rate_prediction: MagicMock)\
        -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_higher(mocked_get_exchange_rate_prediction: MagicMock)\
        -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
