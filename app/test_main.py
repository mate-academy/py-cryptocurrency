from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_higher_more_than_5_percent(exchange_rate_prediction: object) -> None:
    exchange_rate_prediction.return_value = 120
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_lower_more_than_5_percent(exchange_rate_prediction: object) -> None:
    exchange_rate_prediction.return_value = 80
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_difference_less_than_5_percent_1(
        exchange_rate_prediction: object) -> None:
    exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_difference_less_than_5_percent_2(
        exchange_rate_prediction: object) -> None:
    exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
