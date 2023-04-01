from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_current_rate_less(
        mocked_rate_prediction: mock
) -> None:
    mocked_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_rate_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_current_rate_more(
        mocked_rate_prediction: mock
) -> None:
    mocked_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
    mocked_rate_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_call_function_and_buy(mocked_rate_prediction: mock) -> None:
    mocked_rate_prediction.return_value = 105
    assert cryptocurrency_action(90) == "Buy more cryptocurrency"
    mocked_rate_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_call_function_and_sell(mocked_rate_prediction: mock) -> None:
    mocked_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
    mocked_rate_prediction.assert_called_once()
