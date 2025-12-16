from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    current_rate = 1.00
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate:
        mock_rate.return_value = current_rate * 1.06
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
        mock_rate.return_value = current_rate * 0.94
        assert cryptocurrency_action(current_rate) == (
            "Sell all your cryptocurrency")
        mock_rate.return_value = current_rate * 0.95
        assert cryptocurrency_action(current_rate) == "Do nothing"
        mock_rate.return_value = current_rate * 1.05
        assert cryptocurrency_action(current_rate) == "Do nothing"
