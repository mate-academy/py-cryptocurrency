from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mocked_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_exchange_rate_prediction.return_value = 110.0

    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        mocked_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_exchange_rate_prediction.return_value = 90.0

    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_1_05(
        mocked_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_exchange_rate_prediction.return_value = 105.0

    assert cryptocurrency_action(100.0) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_0_95(
        mocked_exchange_rate_prediction: mock.Mock
) -> None:
    mocked_exchange_rate_prediction.return_value = 95.0

    assert cryptocurrency_action(100.0) == "Do nothing"
