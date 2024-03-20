from app.main import cryptocurrency_action
from unittest import mock


def test_much_money() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 54600.48

        assert cryptocurrency_action(51938.40) == "Buy more cryptocurrency"


def test_few_money() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 41550.72

        assert cryptocurrency_action(51938.40) == ("Sell"
                                                   " all your cryptocurrency")


def test_no_change_money() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 54535.32

        assert cryptocurrency_action(51938.40) == "Do nothing"


def test_nothing_095() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1

        assert cryptocurrency_action(0.95) == "Do nothing"


def test_nothing_2() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.9

        assert cryptocurrency_action(2) == "Do nothing"
