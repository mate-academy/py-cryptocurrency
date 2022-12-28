import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_predict() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mocked_prediction:
        yield mocked_prediction


def test_cryptocurrency_action_more_than(mocked_prediction: str) -> None:
    mocked_predict.return_value = 1.08
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_less_than(mocked_prediction: str) -> None:
    mocked_predict.return_value = 0.8
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_donothing(mocked_prediction: str) -> None:
    mocked_predict.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
