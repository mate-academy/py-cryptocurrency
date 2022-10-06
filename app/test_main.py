import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_action:
        yield mock_action


def test_call_get_exchange_rate_higher(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 8
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_call_get_exchange_rate_lower(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 1
    assert cryptocurrency_action(6) == "Sell all your cryptocurrency"


def test_call_get_exchange_rate_bit_lower(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 3.8
    assert cryptocurrency_action(4) == "Do nothing"


def test_call_get_exchange_rate_bit_higher(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 4.2
    assert cryptocurrency_action(4) == "Do nothing"


def test_call_get_exchange_rate_equals(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 12
    assert cryptocurrency_action(12) == "Do nothing"
