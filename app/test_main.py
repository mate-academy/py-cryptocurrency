from unittest.mock import patch

from app.main import cryptocurrency_action


def test_cryptocurrency_action_higher_than_five_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_function:
        mock_function.return_value = 100
        result = cryptocurrency_action(94)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_lower_than_five_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_function:
        mock_function.return_value = 100
        result = cryptocurrency_action(106)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_below_than_five_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_function:
        mock_function.return_value = 100
        result = cryptocurrency_action(104)
        assert result == "Do nothing"


def test_cryptocurrency_action_exactly_five_percent_up() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_function:
        mock_function.return_value = 105
        result = cryptocurrency_action(100)
        assert result == "Do nothing"  # ровно 5%, не больше


def test_cryptocurrency_action_exactly_five_percent_down() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_function:
        mock_function.return_value = 95
        result = cryptocurrency_action(100)
        assert result == "Do nothing"  # ровно -5%, не меньше
