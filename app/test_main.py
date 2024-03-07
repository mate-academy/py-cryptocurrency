from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_called_functions(
        get_exchange_rate_prediction: mock.Mock
) -> None:
    cryptocurrency_action(1)
    get_exchange_rate_prediction.assert_called_once()


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_percen_is_more_than_5(
        get_exchange_rate_prediction: mock.Mock
) -> None:
    cryptocurrency_action(1)
    get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_percen_is_less_than_5(
        get_exchange_rate_prediction: mock.Mock
) -> None:
    cryptocurrency_action(1)
    get_exchange_rate_prediction.return_value = 0.89
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_percen_is_neutral(
        get_exchange_rate_prediction: mock.Mock
) -> None:
    cryptocurrency_action(1)
    get_exchange_rate_prediction.return_value = 0.99
    assert cryptocurrency_action(1) == "Do nothing"
