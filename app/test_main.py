from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=100)
def test_rate_is_more_higher(rate_prediction: float) -> None:
    assert cryptocurrency_action(75) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=60)
def test_rate_is_more_lower(rate_prediction: float) -> None:
    assert cryptocurrency_action(75) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=74)
def test_rate_difference_is_not_that_much(rate_prediction: float) -> None:
    assert cryptocurrency_action(75) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=78.75)
def test_rate_is_higher(rate_prediction: float) -> None:
    assert cryptocurrency_action(75) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=71.25)
def test_rate_is_lower(rate_prediction: float) -> None:
    assert cryptocurrency_action(75) == "Do nothing"
