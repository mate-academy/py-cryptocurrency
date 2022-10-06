from app.main import get_exchange_rate_prediction
from app.main import cryptocurrency_action
from unittest import mock
import pytest


def test_get_exchange_rate_prediction_with_zero() -> None:
    assert get_exchange_rate_prediction(0) == 0.0


def test_get_exchange_rate_prediction_with_any_more_than_zero() -> None:
    assert get_exchange_rate_prediction(0.5) > 0


def test_get_exchange_rate_prediction_with_any_more_than_zero_2() -> None:
    assert get_exchange_rate_prediction(1) > 0


@pytest.fixture()
def mocked_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_prediction:
        yield mock_prediction


def test_should_return_do_nothing_05_percents(mocked_prediction:
                                              mock.MagicMock) -> None:
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing_less_than_05_per(mocked_prediction:
                                                   mock.MagicMock) -> None:
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_buy_more(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 3
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_should_return_sell_all(mocked_prediction: mock.MagicMock) -> None:
    mocked_prediction.return_value = 2
    assert cryptocurrency_action(3) == "Sell all your cryptocurrency"
