import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        yield mocked_prediction


def test_advice_to_buy_more_currency(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_advice_to_sell_all_currency(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 90
    assert cryptocurrency_action(110) == "Sell all your cryptocurrency"


def test_advice_to_do_nothing(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 92
    assert cryptocurrency_action(90) == "Do nothing"


def test_do_nothing(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_else(mocked_prediction: mock) -> None:
    mocked_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
