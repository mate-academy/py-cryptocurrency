from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_higher(mock_rate: mock) -> None:
    mock_rate.return_value = 1.06
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_lower(mock_rate: mock) -> None:
    mock_rate.return_value = 0.94
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_not_difference_high(mock_rate: mock) -> None:
    mock_rate.return_value = 1.05
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_not_difference_low(mock_rate: mock) -> None:
    mock_rate.return_value = 0.95
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Do nothing"
