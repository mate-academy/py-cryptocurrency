from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exchange_rate_prediction(get_exchange_rate_prediction: int) -> None:
    get_exchange_rate_prediction.return_value = 2
    result = cryptocurrency_action(1.05)
    assert "Buy more cryptocurrency" == result


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(get_exchange_rate_prediction: int) -> None:
    get_exchange_rate_prediction.return_value = 1
    result = cryptocurrency_action(1.0)
    assert "Do nothing" == result


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all(get_exchange_rate_prediction: int) -> None:
    get_exchange_rate_prediction.return_value = 0.2
    result = cryptocurrency_action(0.9)
    assert "Sell all your cryptocurrency" == result


@mock.patch("app.main.get_exchange_rate_prediction")
def test_for_exact_ratio(get_exchange_rate_prediction: int) -> None:
    get_exchange_rate_prediction.return_value = 1.05
    result = cryptocurrency_action(1)
    assert "Do nothing" == result


@mock.patch("app.main.get_exchange_rate_prediction")
def test_for_sell_or_buy(get_exchange_rate_prediction: int) -> None:
    get_exchange_rate_prediction.return_value = 0.95
    result = cryptocurrency_action(1)
    assert "Do nothing" == result
