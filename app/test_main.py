import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocking_prediction() -> None:
    with mock.patch("app.main."
                    "get_exchange_rate_prediction") as mocked_prediction:
        yield mocked_prediction


def test_buy_more_cryptocurrency(mocking_prediction: callable) -> None:
    mocking_prediction.return_value = 1.06
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency", (
        "if prediction 5% more than current rate, "
        "it should return 'Buy more cryptocurrency'"
    )


def test_sell_all_cryptocurrency(mocking_prediction: callable) -> None:
    mocking_prediction.return_value = 0.94
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency", (
        "if prediction 5% less than current rate, "
        "it should return 'Sell all your cryptocurrency'"
    )


def test_do_nothing_with_5_percent_more(mocking_prediction: callable) -> None:
    mocking_prediction.return_value = 1.05
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing", (
        "if prediction difference with current rate "
        "is no more than 5%, it should return 'Do nothing'"
    )


def test_do_nothing_with_5_percent_less(mocking_prediction: callable) -> None:
    mocking_prediction.return_value = 0.95
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing", (
        "if prediction difference with current rate "
        "is no more than 5%, it should return 'Do nothing'"
    )


def test_do_nothing_with_between(mocking_prediction: callable) -> None:
    mocking_prediction.return_value = 1.0
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing", (
        "if prediction difference with current rate "
        "is no more than 5%, it should return 'Do nothing'"
    )
