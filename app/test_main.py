from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=8)
def test_check_if_function_was_called(
        mocked_prediction: mock.MagicMock) -> None:
    cryptocurrency_action(98.8)
    mocked_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction", return_value=15)
def test_check_when_we_buy_more(
        mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(12)
    assert current_prediction == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=10)
def test_check_when_we_sell(mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(13.1)
    assert current_prediction == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=5.2)
def test_check_when_do_nothing(mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(5.1)
    assert current_prediction == "Do nothing"
