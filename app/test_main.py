from app.main import cryptocurrency_action

from unittest import mock


def test_cryptocurrency_action_sell_all_cryptocurrency() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 94
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_buy_cryptocurrency() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 106
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action_nothing_cryptocurrency() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 101
        assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action_extreme_case_all_cryptocurrency()\
        -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 95
        assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action_extreme_big_case_all_cryptocurrency()\
        -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 105
        assert cryptocurrency_action(100) == "Do nothing"