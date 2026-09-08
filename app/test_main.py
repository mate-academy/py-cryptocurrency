from unittest.mock import patch
from app.main import cryptocurrency_action


def test_buy_when_prediction_more_than_5_percent_higher() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 106
        assert cryptocurrency_action(current_rate=100) == ("Buy more "
                                                           "cryptocurrency")


def test_sell_when_prediction_more_than_5_percent_lower() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 94
        assert cryptocurrency_action(current_rate=100) == ("Sell all your "
                                                           "cryptocurrency")


def test_do_nothing_on_exact_5_percent_boundaries() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 105
        assert cryptocurrency_action(current_rate=100) == "Do nothing"

        mock_pred.return_value = 95
        assert cryptocurrency_action(current_rate=100) == "Do nothing"


def test_do_nothing_when_change_within_5_percent() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 100
        assert cryptocurrency_action(current_rate=100) == "Do nothing"
