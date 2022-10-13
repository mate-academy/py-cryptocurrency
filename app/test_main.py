from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.fixture()
def mock_func() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        yield mock_func


def test_sell_crypt(mock_func: mock) -> None:
    mock_func.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_buy_crypt(mock_func: mock) -> None:
    mock_func.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_do_nothing(mock_func: mock) -> None:
    mock_func.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_else(mock_func: mock) -> None:
    mock_func.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
