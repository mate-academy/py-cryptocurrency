import app.main as main
from unittest.mock import patch


def test_more_5_percent_than_course() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = 106

        result = main.cryptocurrency_action(100)

        assert result == "Buy more cryptocurrency"


def test_less_5_percent_than_course() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = 94

        result = main.cryptocurrency_action(100)

        assert result == "Sell all your cryptocurrency"


def test_more_than_course_but_less_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = 103

        result = main.cryptocurrency_action(100)

        assert result == "Do nothing"


def test_less_than_course_but_less_than_5() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = 97

        result = main.cryptocurrency_action(100)

        assert result == "Do nothing"


def test_course_more_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = 105

        result = main.cryptocurrency_action(100)

        assert result == "Do nothing"


def test_course_less_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = 95

        result = main.cryptocurrency_action(100)

        assert result == "Do nothing"


def test_course_equal() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_exchange:
        mock_exchange.return_value = 100

        result = main.cryptocurrency_action(100)

        assert result == "Do nothing"
