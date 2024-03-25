from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.fixture()
def mock_func() -> mock.Mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as func_mock:
        yield func_mock


def test_rate_of_106_percent_buy(mock_func: mock.Mock) -> None:
    mock_func.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


def test_rate_of_94_percent_sell(mock_func: mock.Mock) -> None:
    mock_func.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


def test_rate_105_percent_nothing(mock_func: mock.Mock) -> None:
    mock_func.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"


def test_rate_95_percent_nothing(mock_func: mock.Mock) -> None:
    mock_func.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"
