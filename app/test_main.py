from unittest import mock
from unittest.mock import MagicMock

import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_exc_rate:
        yield mock_exc_rate


def test_should_buy_if_prediction_more_then_5_percent_higher(
        mocked_exchange: MagicMock
) -> None:
    mocked_exchange.return_value = 1051
    assert cryptocurrency_action(1000) == "Buy more cryptocurrency"


def test_should_buy_if_prediction_more_then_5_percent_lower(
        mocked_exchange: MagicMock
) -> None:
    mocked_exchange.return_value = 949
    assert cryptocurrency_action(1000) == "Sell all your cryptocurrency"


def test_should_do_nothing_if_not_much_difference_lower(
        mocked_exchange: MagicMock
) -> None:
    mocked_exchange.return_value = 950
    assert cryptocurrency_action(1000) == "Do nothing"


def test_should_do_nothing_if_not_much_difference_higher(
        mocked_exchange: MagicMock
) -> None:
    mocked_exchange.return_value = 1050
    assert cryptocurrency_action(1000) == "Do nothing"
