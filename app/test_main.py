from pytest import fixture

from unittest import mock

from app.main import cryptocurrency_action


@fixture()
def mocked_get_exchange_rate() -> mock.MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        yield mocked_prediction


def test_sell_cryptocurrency(mocked_get_exchange_rate: mock.MagicMock) -> None:
    mocked_get_exchange_rate.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_buy_cryptocurrency(mocked_get_exchange_rate: mock.MagicMock) -> None:
    mocked_get_exchange_rate.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_do_nothing_105_percent(mocked_get_exchange_rate: mock.MagicMock) -> None:
    mocked_get_exchange_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_95_percent(mocked_get_exchange_rate: mock.MagicMock) -> None:
    mocked_get_exchange_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
