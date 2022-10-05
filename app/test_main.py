from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_test:
        yield mocked_test


def test_predicted_rate_is_higher(mocked_rate: None) -> None:
    mocked_rate.return_value = 10
    assert cryptocurrency_action(5) == "Buy more cryptocurrency"


def test_predicted_rate_is_lower(mocked_rate: None) -> None:
    mocked_rate.return_value = 5
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


def test_predicted_rate_is_not_high(mocked_rate: None) -> None:
    mocked_rate.return_value = 5.25
    assert cryptocurrency_action(5) == "Do nothing"


def test_predicted_rate_is_not_low(mocked_rate: None) -> None:
    mocked_rate.return_value = 4.75
    assert cryptocurrency_action(5) == "Do nothing"
