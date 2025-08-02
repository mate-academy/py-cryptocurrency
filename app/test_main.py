import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture
def mock_rate() -> mock:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_exchange_rate:
        yield mock_exchange_rate


def test_should_return_buy_more(mock_rate: mock) -> None:
    mock_exchange_rate = mock_rate
    mock_exchange_rate.return_value = 3
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_should_return_sell_all(mock_rate: mock) -> None:
    mock_exchange_rate = mock_rate
    mock_exchange_rate.return_value = 1
    assert cryptocurrency_action(3) == "Sell all your cryptocurrency"


def test_should_return_do_nothing(mock_rate: mock) -> None:
    mock_exchange_rate = mock_rate
    mock_exchange_rate.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing_1_05(mock_rate: mock) -> None:
    mock_exchange_rate = mock_rate
    mock_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing_0_95(mock_rate: mock) -> None:
    mock_exchange_rate = mock_rate
    mock_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
