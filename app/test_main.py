import random
from unittest import mock
from app.main import cryptocurrency_action


def test_crypt_action_predicted_exchange_rate_is_higher() -> None:
    random.seed(1)
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_crypt_action_predicted_exchange_rate_is_lower() -> None:
    random.seed(5)
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_crypt_action_predicted_exchange_rate_is_not_that_much() -> None:
    random.seed(7)
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_mock(mocked_get: int) -> None:
    mocked_get.return_value = 7
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_mock2(mocked_get: int) -> None:
    mocked_get.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
