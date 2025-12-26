from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_exchange_rate: mock) -> None:
    mock_get_exchange_rate.return_value = 1.1
    result = cryptocurrency_action(1.0)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_exchange_rate: mock) -> None:
    mock_get_exchange_rate.return_value = 0.9
    result = cryptocurrency_action(1.0)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_one_five(mock_get_exchange_rate: mock) -> None:
    mock_get_exchange_rate.return_value = 1.05
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_zero_ninety_five(mock_get_exchange_rate: mock) -> None:
    mock_get_exchange_rate.return_value = 0.95
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"
