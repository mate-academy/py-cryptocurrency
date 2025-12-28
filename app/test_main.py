import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_cryptocurrency() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_test_action:
        yield mock_test_action


def test_get_exchange_rate_higher(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 9
    assert cryptocurrency_action(4) == "Buy more cryptocurrency"


def test_get_exchange_rate_subsides(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 3
    assert cryptocurrency_action(9) == "Sell all your cryptocurrency"


def test_get_exchange_rate_slightly_less(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 3.8
    assert cryptocurrency_action(4) == "Do nothing"


def test_get_exchange_rate_a_bit_more(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 4.2
    assert cryptocurrency_action(4) == "Do nothing"


def test_difference_nothing_difference(mocked_cryptocurrency: None) -> None:
    mocked_cryptocurrency.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"
