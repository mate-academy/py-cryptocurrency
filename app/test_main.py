from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.fixture()
def mock_envision() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") \
            as mock_prediction:
        yield mock_prediction


def test_if_predicted_exchange_rate_is_higher(mock_envision: callable) -> None:
    mock_envision.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_if_predicted_exchange_rate_is_low(mock_envision: callable) -> None:
    mock_envision.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_if_difference_is_not_that_much_1(mock_envision: callable) -> None:
    mock_envision.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_if_difference_is_not_that_much_2(mock_envision: callable) -> None:
    mock_envision.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
