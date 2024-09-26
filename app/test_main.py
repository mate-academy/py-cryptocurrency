from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 2
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_hold(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_lower_boundary(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_upper_boundary(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
