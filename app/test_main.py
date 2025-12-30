import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch


@pytest.fixture
def mocked_exchange_rate() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_buy_more_cryptocurrency(mocked_exchange_rate: int) -> None:
    current_rate = 100
    mocked_exchange_rate.return_value = 108
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency(mocked_exchange_rate: int) -> None:
    current_rate = 100
    mocked_exchange_rate.return_value = 94
    assert (cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency")


def test_buy_more_cryptocurrency2(mocked_exchange_rate: int) -> None:
    current_rate = 100
    mocked_exchange_rate.return_value = 105
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_sell_all_your_cryptocurrency1(mocked_exchange_rate: int) -> None:
    current_rate = 100
    mocked_exchange_rate.return_value = 95
    assert cryptocurrency_action(current_rate) == "Do nothing"
