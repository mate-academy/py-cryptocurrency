from unittest import mock
import app.main


def test_if_rate_prediction_more_than_five() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = 106
        assert app.main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_if_rate_prediction_equal_five() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = 105
        assert app.main.cryptocurrency_action(100) == "Do nothing"


def test_if_rate_prediction_equal_zero() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = 100
        assert app.main.cryptocurrency_action(100) == "Do nothing"


def test_if_rate_prediction_equal_five_minus() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = 95
        assert app.main.cryptocurrency_action(100) == "Do nothing"


def test_if_rate_prediction_less_than_five() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = 94
        assert (
            app.main.cryptocurrency_action(100)
            == "Sell all your cryptocurrency"
        )
