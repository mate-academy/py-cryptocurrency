import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.fixture
def random_choice() -> None:
    with mock.patch("random.choice") as get_random_choice:
        yield get_random_choice


@pytest.fixture
def random_random() -> None:
    with mock.patch("random.random") as get_random_random:
        yield get_random_random


def test_should_return_buy_more_cryptocurrency(
        random_choice: mock,
        random_random: mock
) -> None:
    # preparation
    current_rate = 100

    # changing return value
    random_choice.return_value = "increase"
    random_random.return_value = 0.952

    # assertion
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_should_return_sell_all_cryptocurrency(
        random_choice: mock,
        random_random: mock
) -> None:
    # preparation
    current_rate = 100

    # changing return value
    random_choice.return_value = "decrease"
    random_random.return_value = 0.949

    # assertion
    assert cryptocurrency_action(
        current_rate
    ) == "Sell all your cryptocurrency"


def test_should_return_do_nothing_with_decrease_rate(
        random_choice: mock,
        random_random: mock
) -> None:
    # preparation
    current_rate = 100

    # changing return value
    random_choice.return_value = "decrease"
    random_random.return_value = 0.95

    # assertion
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_should_return_do_nothing_with_increase_rate(
        random_choice: mock,
        random_random: mock
) -> None:
    # preparation
    current_rate = 100

    # changing return value
    random_choice.return_value = "increase"
    random_random.return_value = 0.9524

    # assertion
    assert cryptocurrency_action(current_rate) == "Do nothing"
