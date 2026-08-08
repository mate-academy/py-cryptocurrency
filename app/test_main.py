import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.fixture()
def current_rate_template() -> float:
    current_rate = 100.0
    return current_rate


def test_exchange_rate_higher_than_current(
        current_rate_template: float) -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=106.0):
        assert cryptocurrency_action(current_rate_template
                                     ) == "Buy more cryptocurrency"


def test_exchange_rate_lower_than_current(
        current_rate_template: float) -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=94.0):
        assert cryptocurrency_action(current_rate_template
                                     ) == "Sell all your cryptocurrency"


def test_difference_exchange_rate_is_not_much(
        current_rate_template: float) -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=97.0):
        assert cryptocurrency_action(current_rate_template) == "Do nothing"

    with patch("app.main.get_exchange_rate_prediction", return_value=103.0):
        assert cryptocurrency_action(current_rate_template) == "Do nothing"


def test_should_not_sell_cryptocurrency_when_equal_to_condition(
        current_rate_template: float) -> None:
    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        assert cryptocurrency_action(current_rate_template) == "Do nothing"
    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        assert cryptocurrency_action(current_rate_template) == "Do nothing"
