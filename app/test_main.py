from app.main import cryptocurrency_action
from unittest import mock


class TestExchange:
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self, mocked_transfer):
        mocked_transfer.return_value = 2
        assert cryptocurrency_action(1.1) == "Buy more cryptocurrency"
        assert cryptocurrency_action(3) == "Sell all your cryptocurrency"
        assert cryptocurrency_action(2) == "Do nothing"
        mocked_transfer.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"
        mocked_transfer.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"
