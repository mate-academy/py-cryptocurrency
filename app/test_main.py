import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_predict() -> mock:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_prediction:
        yield mock_prediction


def test_buy(mocked_predict: mock) -> None:
    mocked_predict.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell(mocked_predict: mock) -> None:
    mocked_predict.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_nothing_to_do_min(mocked_predict: mock) -> None:
    mocked_predict.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_nothing_to_do_max(mocked_predict: mock) -> None:
    mocked_predict.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
