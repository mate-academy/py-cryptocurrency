from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_need_buy(mock_rate_prediction):
    mock_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_sell(mock_rate_prediction):
    mock_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_need_do_nothing(mock_rate_prediction):
    mock_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_need_do_nothing2(mock_rate_prediction):
    mock_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
