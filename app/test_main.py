from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_low_rating(mock_function: int) -> None:
    mock_function.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_high_rating(mock_function: int) -> None:
    mock_function.return_value = 105.1
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_not_difference_rating(mock_function: int) -> None:
    mock_function.return_value = 95.1
    assert cryptocurrency_action(100) == "Do nothing"
