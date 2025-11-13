from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=100)
def test_do_nothing(mock_prediction: mock.MagicMock) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=190)
def test_buy_more_cryptocurrency(mock_prediction: mock.MagicMock) -> None:
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=90)
def test_sell_all_cryptocurrency(mock_prediction: mock.MagicMock) -> None:
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_do_nothing_limit_value(mock_prediction: mock.MagicMock) -> None:
    assert cryptocurrency_action(100) == "Do nothing"
