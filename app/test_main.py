from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 10

    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all_your_cryptocurrency(
        mock_get_exchange_rate_prediction: any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 2

    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing(
        mock_get_exchange_rate_prediction: any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 9.5

    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_nothing(
        mock_get_exchange_rate_prediction: any
) -> None:
    mock_get_exchange_rate_prediction.return_value = 10.5

    assert cryptocurrency_action(10) == "Do nothing"
