from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_low_rating(mock_function: int) -> None:
    mock_function.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_high_rating(mock_function: int) -> None:
    mock_function.return_value = 107
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_between_rating(mock_function: int) -> None:
    mock_function.return_value = 96
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_equal_high_rating(mock_function: int) -> None:
    mock_function.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_equal_low_rating(mock_function: int) -> None:
    mock_function.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
