import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_get_exchange_rate_prediction:
        mocked_get_exchange_rate_prediction.return_value = 94.0
        yield mocked_get_exchange_rate_prediction


@pytest.fixture
def mocked_get_exchange_rate_prediction2() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_get_exchange_rate_prediction:
        mocked_get_exchange_rate_prediction.return_value = 106.0
        yield mocked_get_exchange_rate_prediction


@pytest.fixture
def mocked_get_exchange_rate_prediction3() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_get_exchange_rate_prediction:
        mocked_get_exchange_rate_prediction.return_value = 105.0
        yield mocked_get_exchange_rate_prediction


@pytest.fixture
def mocked_get_exchange_rate_prediction4() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_get_exchange_rate_prediction:
        mocked_get_exchange_rate_prediction.return_value = 95.0
        yield mocked_get_exchange_rate_prediction


def test_cryptocurrency_action4(
        mocked_get_exchange_rate_prediction4: any
) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action3(
        mocked_get_exchange_rate_prediction3: any
) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action2(
        mocked_get_exchange_rate_prediction2: any
) -> None:
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: any
) -> None:
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
