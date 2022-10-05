from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_cryptocurrency_test() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_test:
        yield mocked_test


def test_for_sale(mocked_cryptocurrency_test: int) -> None:
    mocked_cryptocurrency_test.return_value = 120
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_for_buy(mocked_cryptocurrency_test: int) -> None:
    mocked_cryptocurrency_test.return_value = 100
    assert cryptocurrency_action(120) == "Sell all your cryptocurrency"


def test_for_do_nothing_percen_bigger(mocked_cryptocurrency_test: float
                                      ) -> None:
    mocked_cryptocurrency_test.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_percent_less_five(mocked_cryptocurrency_test: float
                                      ) -> None:
    mocked_cryptocurrency_test.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
