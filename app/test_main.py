import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> float:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_test_random:
        yield mock_test_random


def test_buy_more_cryptocurrency(
        mocked_get_exchange_rate_prediction: float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency(
        mocked_get_exchange_rate_prediction: float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_to_nothing_for_your_cryptocurrency(
        mocked_get_exchange_rate_prediction: float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_raise_zero_division_error_if_values_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
