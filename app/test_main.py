from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as get_rate:
        yield get_rate


def test_cryptocurrency_action_with_mock_buy_more(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.3
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_with_mock_sell_all(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.3
    assert cryptocurrency_action(7) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_with_mock_do_nothing_than_1_05(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_action_with_mock_do_nothing_than_0_95(
        mocked_get_exchange_rate_prediction: mock
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
