from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 1.1
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.9
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_95(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.95
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_105(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 1.05
    current_rate = 1.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
