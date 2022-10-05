from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_minor_profit(mocked_prediction
                                            : float) -> None:
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_minor_loss(mocked_prediction
                                          : float) -> None:
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_huge_profit(mocked_prediction
                                           : float) -> None:
    mocked_prediction.return_value = 3
    assert cryptocurrency_action(1.5) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_huge_loss(mocked_prediction
                                         : float) -> None:
    mocked_prediction.return_value = 1
    assert cryptocurrency_action(3) == "Sell all your cryptocurrency"
