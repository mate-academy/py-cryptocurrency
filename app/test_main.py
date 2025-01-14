from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_prediction_more_than_5_percents(
        mocked_prediction: any
) -> None:
    mocked_prediction.return_value = 1.06

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"

    mocked_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_prediction_less_than_5_percents(
        mocked_prediction: any
) -> None:
    mocked_prediction.return_value = 0.94

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

    mocked_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_prediction_in_smaller_range(
        mocked_prediction: any
) -> None:
    mocked_prediction.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"

    mocked_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_prediction_in_bigger_range(
        mocked_prediction: any
) -> None:
    mocked_prediction.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"

    mocked_prediction.assert_called_once()
