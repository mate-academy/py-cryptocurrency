from unittest.mock import MagicMock, patch
from app import main
from pytest import fixture


@fixture()
def mocked_get_erp() -> MagicMock:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


def test_return_buy_more(mocked_get_erp: MagicMock) -> None:
    mocked_get_erp.return_value = 50
    assert main.cryptocurrency_action(40) == "Buy more cryptocurrency"


def test_return_sell_all(mocked_get_erp: MagicMock) -> None:
    mocked_get_erp.return_value = 40
    assert main.cryptocurrency_action(43) == "Sell all your cryptocurrency"


def test_return_do_nothing(mocked_get_erp: MagicMock) -> None:
    mocked_get_erp.return_value = 105
    assert main.cryptocurrency_action(100) == "Do nothing"
    mocked_get_erp.return_value = 95
    assert main.cryptocurrency_action(100) == "Do nothing"
