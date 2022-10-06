from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_cryptocurrency() -> mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_predict:
        yield mocked_predict


def test_rate_get_higher(mocked_cryptocurrency: mock) -> None:
    mocked_cryptocurrency.return_value = 1.15
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_rate_get_lower(mocked_cryptocurrency: mock) -> None:
    mocked_cryptocurrency.return_value = 0.86
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_rate_get_little_higher(mocked_cryptocurrency: mock) -> None:
    mocked_cryptocurrency.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_get_little_lower(mocked_cryptocurrency: mock) -> None:
    mocked_cryptocurrency.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_equal_current(mocked_cryptocurrency: mock) -> None:
    mocked_cryptocurrency.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"
