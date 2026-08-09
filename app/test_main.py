from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 1.1
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_95(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_105(mock_exchange_rate: mock) -> None:
    mock_exchange_rate.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
