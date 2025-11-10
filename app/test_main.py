from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.fixture(scope="module")
def rate_prediction() -> mock:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction):
        yield mocked_prediction


def test_when_result_is_equal_1_05(rate_prediction: mock) -> None:
    rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_when_result_is_equal_0_95(rate_prediction: mock) -> None:
    rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_when_result_is_less_than_0_95(rate_prediction: mock) -> None:
    rate_prediction.return_value = 0.95
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_when_result_is_greater_than_1_05(
        rate_prediction: int | float) -> None:
    rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
