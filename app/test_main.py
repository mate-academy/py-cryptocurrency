from app.main import cryptocurrency_action

from unitest import mock


def test_cryptocurrency_action_sell_all_cryptocurrency():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 94
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_buy_cryptocurrency():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 105
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action_nothing_cryptocurrency():
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = 101
        assert cryptocurrency_action(100) == "Do nothing"
