from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=8)
def test_check_if_function_was_called(
        mocked_prediction: mock.MagicMock) -> None:
    cryptocurrency_action(98.8)
    mocked_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction", return_value=15.1)
def test_check_when_we_buy_more(
        mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(12)
    assert current_prediction == "Buy more cryptocurrency"


@mock.patch(
    "app.main.get_exchange_rate_prediction", return_value=3760)
def test_check_when_we_sell(
        mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(4000)
    assert current_prediction == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=5.25)
def test_check_when_do_nothing(mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(5.1)
    assert current_prediction == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=12.6)
def test_rate_105_percent_do_nothing(
        mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(12)
    assert current_prediction == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=9.5)
def test_rate_95_percent_do_nothing(
        mocked_rate_prediction: mock.MagicMock) -> None:
    current_prediction = cryptocurrency_action(10)
    assert current_prediction == "Do nothing"
