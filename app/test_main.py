from unittest.mock import patch
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange_rate_prediction:
        mock_get_exchange_rate_prediction.return_value = 1.06
        result = cryptocurrency_action(1)
        assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange_rate_prediction:
        mock_get_exchange_rate_prediction.return_value = 0.94
        result = cryptocurrency_action(1)
        assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange_rate_prediction:
        mock_get_exchange_rate_prediction.return_value = 1.03
        result = cryptocurrency_action(1)
        assert result == "Do nothing"


def test_cryptocurrency_action_boundary_0_95() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange_rate_prediction:
        mock_get_exchange_rate_prediction.return_value = 0.95
        result = cryptocurrency_action(1)
        assert result == "Do nothing"


def test_cryptocurrency_action_boundary_1_05() -> None:
    with patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_get_exchange_rate_prediction:
        mock_get_exchange_rate_prediction.return_value = 1.05
        result = cryptocurrency_action(1)
        assert result == "Do nothing"
