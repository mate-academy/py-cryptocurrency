import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture
def mocked_get_exchange_rate() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction") as
          mock_exchange_rate):
        yield mock_exchange_rate


def test_cryptocurrency_with_exchange_going_up(
        mocked_get_exchange_rate: mock
) -> None:
    mocked_get_exchange_rate.return_value = 200
    result = cryptocurrency_action(10)

    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_with_exchange_below(
        mocked_get_exchange_rate: mock
) -> None:
    mocked_get_exchange_rate.return_value = 9.42
    result = cryptocurrency_action(10)

    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_with_exchange_between(
        mocked_get_exchange_rate: mock
) -> None:
    mocked_get_exchange_rate.return_value = 10.50
    result = cryptocurrency_action(10)

    assert result == "Do nothing"


def test_cryptocurrency_with_exchange_between_second(
        mocked_get_exchange_rate: mock
) -> None:
    mocked_get_exchange_rate.return_value = 9.50
    result = cryptocurrency_action(10)

    assert result == "Do nothing"
