from app.main import cryptocurrency_action

from unittest import mock


def test_cryptocurrency_action_when_rate_high() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=106) as mock_rate:
        result = cryptocurrency_action(100)
        mock_rate.assert_called_once()
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_when_rate_low() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=94) as mock_rate:
        result = cryptocurrency_action(100)
        mock_rate.assert_called_once()
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_when_prediction_average() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = 95
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
        mock_rate.return_value = 105
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
