from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_105(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 4.53
    assert cryptocurrency_action(3) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_095(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.5
    assert cryptocurrency_action(3) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_exep105(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_end_case095(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
