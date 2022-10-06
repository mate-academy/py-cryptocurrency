import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_action:
        yield mock_action


def test_get_exchange_rate_higher(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 10
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_get_exchange_rate_lower(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 7
    assert cryptocurrency_action(15) == "Sell all your cryptocurrency"


def test_get_exchange_rate_bit_higher(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 6
    assert cryptocurrency_action(6.2) == "Do nothing"


def test_get_exchange_rate_bit_lower(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 5
    assert cryptocurrency_action(4.8) == "Do nothing"
