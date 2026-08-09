from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_minor_profit(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_minor_loss(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_huge_profit(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 30
    assert cryptocurrency_action(15) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_huge_loss(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 10
    assert cryptocurrency_action(30) == "Sell all your cryptocurrency"
