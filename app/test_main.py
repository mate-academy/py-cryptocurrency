import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_test:
        yield mocked_test


def test_to_buy_more(mocked_rate_prediction: float) -> None:
    mocked_rate_prediction.return_value = 12
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_sell_all(mocked_rate_prediction: float) -> None:
    mocked_rate_prediction.return_value = 8
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


def test_to_do_nothing(mocked_rate_prediction: float) -> None:
    mocked_rate_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


def test_to_do_nothing_with_lower_value(mocked_rate_prediction: float) -> None:
    mocked_rate_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"

