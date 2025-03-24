from unittest.mock import patch
from app.main import cryptocurrency_action


def test_should_buy_more_when_predicted_rate_more_than_5_percent_higher()\
        -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 105.01
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_should_sell_all_when_predicted_rate_more_than_5_percent_lower()\
        -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 94.99
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_do_nothing_when_predicted_rate_within_5_percent() -> None:
    test_cases = [105, 95, 104.999, 95.001, 102, 98]
    for rate in test_cases:
        with patch("app.main.get_exchange_rate_prediction") as mock_pred:
            mock_pred.return_value = rate
            assert cryptocurrency_action(100) == "Do nothing"


def test_exact_5_percent_changes() -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 105
        assert cryptocurrency_action(100) == "Do nothing"

    with patch("app.main.get_exchange_rate_prediction") as mock_pred:
        mock_pred.return_value = 95
        assert cryptocurrency_action(100) == "Do nothing"
