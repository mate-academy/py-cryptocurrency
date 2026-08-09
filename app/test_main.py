from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        current_rate = 10

        mock_get_exchange_rate_prediction.return_value = 10.5
        assert cryptocurrency_action(current_rate) == "Do nothing"

        mock_get_exchange_rate_prediction.return_value = 9.5
        assert cryptocurrency_action(current_rate) == "Do nothing"
