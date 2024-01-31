from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction():
    with mock.patch('app.main.get_exchange_rate_prediction') \
            as mocked_rate_prediction:
        yield mocked_rate_prediction


@pytest.mark.parametrize(
    "exchange_rate,current_rate,expected",
    [
        (
            1,
            1,
            "Do nothing"
        ),
        (
            1.05,
            1,
            "Do nothing"
        ),
        (
            0.95,
            1,
            "Do nothing"
        ),
        (
            1.4,
            1,
            "Buy more cryptocurrency"
        ),
        (
            0.4,
            1,
            "Sell all your cryptocurrency"
        )
    ]
)
def test_cryptocurrency_do_nothing(mocked_get_exchange_rate_prediction,
                                   exchange_rate,
                                   current_rate,
                                   expected):
    mocked_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == expected
