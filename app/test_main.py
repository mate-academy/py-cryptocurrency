import pytest
from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):

        mock_get_exchange_rate_prediction.return_value = 105.1
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"

        mock_get_exchange_rate_prediction.return_value = 94.9
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

        mock_get_exchange_rate_prediction.return_value = 105.0
        assert cryptocurrency_action(100) == "Do nothing"

        mock_get_exchange_rate_prediction.return_value = 95.0
        assert cryptocurrency_action(100) == "Do nothing"

        mock_get_exchange_rate_prediction.return_value = 104.9
        assert cryptocurrency_action(100) == "Do nothing"

        mock_get_exchange_rate_prediction.return_value = 95.1
        assert cryptocurrency_action(100) == "Do nothing"


if __name__ == "__main__":
    pytest.main()
