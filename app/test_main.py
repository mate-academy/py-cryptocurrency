from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_cryptocurrency(mock_rate_prediction) -> None:
    mock_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency(mock_rate_prediction) -> None:
    mock_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_highest_rate(mock_rate_prediction) -> None:
    mock_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lowest_rate(mock_rate_prediction) -> None:
    mock_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
