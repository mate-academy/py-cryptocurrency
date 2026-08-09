from unittest import mock
from app.main import cryptocurrency_action


def test_buy_more() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 106
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 90
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 99
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_edge_95() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 95
        assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_edge_105() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_predict:
        mock_predict.return_value = 105
        assert cryptocurrency_action(100) == "Do nothing"
