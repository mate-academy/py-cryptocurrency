from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 1.07
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.90
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_95_percent(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_105_percent(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
