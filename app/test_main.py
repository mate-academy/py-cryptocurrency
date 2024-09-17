from unittest import mock
import pytest
from app.main import cryptocurrency_action
from typing import Union


@pytest.fixture()
def mocked_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mocked_prediction:
        yield mocked_prediction


def test_buy_more_cryptocurrency(
        mocked_exchange_rate_prediction: Union[int, float]
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency(
        mocked_exchange_rate_prediction: Union[int, float]
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_rate_105_percent_do_nothing(
        mocked_exchange_rate_prediction: Union[int, float]
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_95_percent_do_nothing(
        mocked_exchange_rate_prediction: Union[int, float]
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
