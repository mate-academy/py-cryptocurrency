from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(
        mocked_get_exchange_rate_prediction: int
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 2
    assert cryptocurrency_action(2.1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_bye(
        mocked_get_exchange_rate_prediction: int
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 2
    assert cryptocurrency_action(1.9) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mocked_get_exchange_rate_prediction: int
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"
