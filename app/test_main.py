from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_higher(mock_rate: mock) -> None:
    mock_rate.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_lower(mock_rate: mock) -> None:
    mock_rate.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_not_difference_high(mock_rate: mock) -> None:
    mock_rate.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_exchange_not_difference_low(mock_rate: mock) -> None:
    mock_rate.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"
