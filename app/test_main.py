from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:

        mock_prediction.return_value = 0.9
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

        mock_prediction.return_value = 1.1
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"

        mock_prediction.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"

        mock_prediction.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"
