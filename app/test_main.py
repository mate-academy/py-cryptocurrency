from pytest import mark
from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mock_get_exchange_rate_prediction():
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        yield mocked_prediction


def test_buy_cryptocurrency_action(mock_get_exchange_rate_prediction) -> None:
    mock_get_exchange_rate_prediction.return_value = 10
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_cryptocurrency_action(mock_get_exchange_rate_prediction) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_do_nothing_cryptocurrency_action(mock_get_exchange_rate_prediction) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"
