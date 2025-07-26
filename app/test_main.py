from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_higher(
        mock_get_exchange_rate_prediction: bool) -> None:
    mock_get_exchange_rate_prediction.return_value = 100
    assert cryptocurrency_action(94) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_lower(
        mock_get_exchange_rate_prediction: bool) -> None:
    mock_get_exchange_rate_prediction.return_value = 100
    assert cryptocurrency_action(106) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_nothing_changed(
        mock_get_exchange_rate_prediction: bool) -> None:
    mock_get_exchange_rate_prediction.return_value = 100
    assert cryptocurrency_action(103) == "Do nothing"
    assert cryptocurrency_action(96) == "Do nothing"
