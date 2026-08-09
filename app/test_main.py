from typing import Callable

import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.fixture
def prediction_mock() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_buy_more(prediction_mock: Callable) -> None:
    prediction_mock.return_value = 106.00
    assert cryptocurrency_action(100.00) == "Buy more cryptocurrency"


def test_sell_all(prediction_mock: Callable) -> None:
    prediction_mock.return_value = 94.00
    assert cryptocurrency_action(100.00) == "Sell all your cryptocurrency"


def test_do_nothing_when_small_difference(prediction_mock: Callable) -> None:
    prediction_mock.return_value = 102.00
    assert cryptocurrency_action(100.00) == "Do nothing"


def test_do_nothing_when_margin_increase(prediction_mock: Callable) -> None:
    prediction_mock.return_value = 105.00
    assert cryptocurrency_action(100.00) == "Do nothing"


def test_do_nothing_when_margin_decrease(prediction_mock: Callable) -> None:
    prediction_mock.return_value = 95.00
    assert cryptocurrency_action(100.00) == "Do nothing"
