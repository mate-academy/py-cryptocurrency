from app.main import cryptocurrency_action
from unittest import mock


def test_get_exchange_rate_prediction() -> None:
    with (mock.patch("random.choice") as mock_choice,
          mock.patch("random.random", return_value=1.25)):
        mock_choice.side_effect = "increase"
        result = cryptocurrency_action(100 / 1.25)
        assert result == "Buy more cryptocurrency"


def test_get_exchange_rate_prediction1() -> None:
    with (mock.patch("random.choice") as mock_choice,
          mock.patch("random.random", return_value=0.7)):
        mock_choice.side_effect = "decrease"
        result = cryptocurrency_action(100 * 0.7)
        assert result == "Sell all your cryptocurrency"


def test_get_exchange_rate_prediction2() -> None:
    with (mock.patch("random.choice") as mock_choice,
          mock.patch("random.random", return_value=1.05)):
        mock_choice.side_effect = "do_nothing"
        result = cryptocurrency_action(100 * 1.05)
        assert result == "Do nothing"


def test_get_exchange_rate_prediction3() -> None:
    with (mock.patch("random.choice") as mock_choice,
          mock.patch("random.random", return_value=0.95)):
        mock_choice.side_effect = "do_nothing"
        result = cryptocurrency_action(100 * 0.95)
        assert result == "Do nothing"
