from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.fixture
def mocked_get_exchange_rate_prediction() -> mock.MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mocked_prediction:
        yield mocked_prediction


def test_rate_95_percent_do_nothing(mocked_get_exchange_rate_prediction
                                    : mock.MagicMock)\
        -> AssertionError:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_rate_105_percent_do_nothing(mocked_get_exchange_rate_prediction
                                     : mock.MagicMock)\
        -> AssertionError:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
