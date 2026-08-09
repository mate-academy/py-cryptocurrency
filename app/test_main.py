import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        yield mocked_rate


def test_if_predicted_rate_higher(
        mocked_prediction: float
) -> None:
    mocked_prediction.return_value = 1.10
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_if_predicted_rate_lower(
        mocked_prediction: float
) -> None:
    mocked_prediction.return_value = 0.90
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_if_predicted_rate_in_5_percent_range(
        mocked_prediction: float
) -> None:
    mocked_prediction.return_value = 1.00
    assert cryptocurrency_action(1) == "Do nothing"


def test_if_predicted_rate_on_the_upper_limit(
        mocked_prediction: float
) -> None:
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_if_predicted_rate_on_the_lower_limit(
        mocked_prediction: float
) -> None:
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
