from app.main import cryptocurrency_action

from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_first(action: any) -> None:
    action.return_value = 2
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_second(action: any) -> None:
    action.return_value = 0.5
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_third(action: any) -> None:
    action.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_fourth(action: any) -> None:
    action.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
