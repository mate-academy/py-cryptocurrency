from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_rate_1(mock_get_rate) -> None:
    mock_get_rate.return_value = 1

    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_rate_095(mock_get_rate) -> None:
    mock_get_rate.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_rate_105(mock_get_rate) -> None:
    mock_get_rate.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_rate_080(mock_get_rate) -> None:
    mock_get_rate.return_value = 0.80

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_rate_120(mock_get_rate) -> None:
    mock_get_rate.return_value = 1.20

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"
