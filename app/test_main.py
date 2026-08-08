from unittest import mock

from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mock_prediction:
        mock_prediction.return_value = 110
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"

        mock_prediction.return_value = 90
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

        mock_prediction.return_value = 105
        assert cryptocurrency_action(100) == "Do nothing"

        mock_prediction.return_value = 95
        assert cryptocurrency_action(100) == "Do nothing"
