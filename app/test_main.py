import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_func:
        yield mocked_func


def test_with_buy_more(mocked_get_exchange_rate_prediction: mock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.5
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_with_sell_all(mocked_get_exchange_rate_prediction: mock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_get_exchange_rate_prediction: mock) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_extreme_digital_value(
        mocked_get_exchange_rate_prediction: mock
) -> None:

    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
