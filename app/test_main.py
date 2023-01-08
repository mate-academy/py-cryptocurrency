from unittest import mock

import pytest as pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exch_rate_pred() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_prediction:
        yield mocked_prediction


def test_do_nothing(mocked_exch_rate_pred: object) -> None:
    mocked_exch_rate_pred.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_if_rate_hight(mocked_exch_rate_pred: object) -> None:
    mocked_exch_rate_pred.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_if_rate_low(mocked_exch_rate_pred: object) -> None:
    mocked_exch_rate_pred.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_by_more_cryptocurrency(mocked_exch_rate_pred: object) -> None:
    mocked_exch_rate_pred.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency(mocked_exch_rate_pred: object) -> None:
    mocked_exch_rate_pred.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
