from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_function:
        yield mock_function


def test_difference_more_5_higher_from_current(
        mocked_get_exchange_rate_prediction: float) -> None:
    mocked_get_exchange_rate_prediction.return_value = 107
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_difference_more_5_lower_from_cur(
        mocked_get_exchange_rate_prediction: float) -> None:
    mocked_get_exchange_rate_prediction.return_value = 30
    assert cryptocurrency_action(60) == "Sell all your cryptocurrency"


def test_dif_less_5_1(
        mocked_get_exchange_rate_prediction: float) -> None:
    mocked_get_exchange_rate_prediction.return_value = 301.0
    assert cryptocurrency_action(300.00) == "Do nothing"


def test_dif_less_5_2(
        mocked_get_exchange_rate_prediction: float) -> None:
    mocked_get_exchange_rate_prediction.return_value = 299.0
    assert cryptocurrency_action(300.00) == "Do nothing"
