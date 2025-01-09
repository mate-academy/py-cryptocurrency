from app.main import cryptocurrency_action
from unittest.mock import patch

def test_cryptocurrency_action_high() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 25
        assert cryptocurrency_action(20) == "Buy more cryptocurrency"


def test_cryptocurrency_action_low() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 15
        assert cryptocurrency_action(20) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_stable() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 23.5
        assert cryptocurrency_action(23) == "Do nothing"


def test_cryptocurrency_action_105() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 21
        assert cryptocurrency_action(20) == "Do nothing"


def test_cryptocurrency_action_095() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = 19
        assert cryptocurrency_action(20) == "Do nothing"