from unittest import mock
import pytest


from .main import cryptocurrency_action


@pytest.fixture
def mock_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as s:
        yield s


def test_should_buy_more(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_should_sell_all(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_dont_do_anything_if_1(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_dont_do_anything_if_095(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_dont_do_anything_if_105(mock_exchange_rate_prediction: any) -> None:
    mock_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
