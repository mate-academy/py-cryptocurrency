from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_rate_105_percent_do_nothing(
        mock_exchange_rate_prediction: float) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_rate_95_percent_do_nothing(
        mock_exchange_rate_prediction: float) -> None:
    assert cryptocurrency_action(1) == "Do nothing"
