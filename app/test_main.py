from app.main import cryptocurrency_action

from unittest import mock


def test_when_increase() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=1.06
    ) as mock_prediction:
        result = cryptocurrency_action(1)
        mock_prediction.assert_called_once()
        assert result == "Buy more cryptocurrency"


def test_when_decrease() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=0.94
    ) as mock_prediction:
        result = cryptocurrency_action(1)
        mock_prediction.assert_called_once()
        assert result == "Sell all your cryptocurrency"


def test_when_rate105() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=1.05
    ) as mock_prediction:
        result = cryptocurrency_action(1)
        mock_prediction.assert_called_once()
        assert result == "Do nothing"


def test_when_rate95() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction", return_value=0.95
    ) as mock_prediction:
        result = cryptocurrency_action(1)
        mock_prediction.assert_called_once()
        assert result == "Do nothing"
