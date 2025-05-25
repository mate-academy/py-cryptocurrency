from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 2.0
    result = cryptocurrency_action(2)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 4.0
    result = cryptocurrency_action(2)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_not_buy(mocked_prediction: float) -> None:
    mocked_prediction.return_value = 1.0
    result = cryptocurrency_action(2)
    assert result == "Sell all your cryptocurrency"
