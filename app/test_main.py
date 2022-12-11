from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_was_called(
    mocked_prediction: object
) -> None:
    mocked_prediction.return_value = 1

    cryptocurrency_action(1)

    mocked_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more_cryptocurrency(
    mocked_prediction: object
) -> None:
    mocked_prediction.return_value = 1.06

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing(
    mocked_prediction: object
) -> None:
    mocked_prediction.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"

    mocked_prediction.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all_your_cryptocurrency(
    mocked_prediction: object
) -> None:
    mocked_prediction.return_value = 0.94

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
