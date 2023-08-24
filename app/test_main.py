from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_random() -> Mock:
    with mock.patch("app.main.random.random") as mock_random:
        yield mock_random


@mock.patch("app.main.random.choice", return_value="increase")
def test_if_exchange_rate_increase(
        mocked_choice: Mock,
        mocked_random: Mock
) -> None:
    mocked_random.return_value = 0.94
    assert cryptocurrency_action(1.2) == "Buy more cryptocurrency"


@mock.patch("app.main.random.choice", return_value="decrease")
def test_if_exchange_rate_decrease(
        mocked_choice: Mock,
        mocked_random: Mock
) -> None:
    mocked_random.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.random.choice", return_value="increase")
def test_if_rate_increase_and_prediction_rate_bigger(
        mocked_choice: Mock,
        mocked_random: Mock
) -> None:
    mocked_random.return_value = 1.05
    assert cryptocurrency_action(1.2) == "Do nothing"


@mock.patch("app.main.random.choice", return_value="decrease")
def test_if_if_rate_decrease_and_prediction_rate_smaller(
        mocked_choice: Mock,
        mocked_random: Mock
) -> None:
    mocked_random.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
