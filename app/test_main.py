import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture
def get_prediction() -> mock.MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_nothing:
        yield mock_nothing


def test_cryptocurrency_action_buy_more(get_prediction: object) -> None:
    get_prediction.return_value = 1.06
    assert cryptocurrency_action(1.00) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(get_prediction: object) -> None:
    get_prediction.return_value = 0.94
    assert cryptocurrency_action(1.00) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(get_prediction: object) -> None:
    get_prediction.return_value = 1.02
    assert cryptocurrency_action(1.00) == "Do nothing"


def test_105(get_prediction: object) -> None:
    get_prediction.return_value = 1.05
    assert cryptocurrency_action(1.00) == "Do nothing"


def test_095(get_prediction: object) -> None:
    get_prediction.return_value = 0.95
    assert cryptocurrency_action(1.00) == "Do nothing"
