from unittest.mock import patch
from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.side_effect = [105, 94, 102, 98]

        assert cryptocurrency_action(100) == "Buy more cryptocurrency"
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
        assert cryptocurrency_action(100) == "Do nothing"
        assert cryptocurrency_action(100) == "Do nothing"
