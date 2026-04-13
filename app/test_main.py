from typing import Generator
from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def get_exchange() -> Generator[MagicMock]:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        yield mock_get_exchange_rate_prediction


def test_do_nothing(get_exchange: MagicMock) -> None:
    get_exchange.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_sell_all_cryptocurrency(get_exchange: MagicMock) -> None:
    get_exchange.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_buy_all_cryptocurrency(get_exchange: MagicMock) -> None:
    get_exchange.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_edge_buy_all_cryptocurrency(get_exchange: MagicMock) -> None:
    get_exchange.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_edge_sell_all_cryptocurrency(get_exchange: MagicMock) -> None:
    get_exchange.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
