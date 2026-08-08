import pytest

from app.main import cryptocurrency_action

from unittest.mock import patch


def test_cryptocurrency_action_correct_result() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_prediction_rate):

        mock_prediction_rate.return_value = 8
        assert cryptocurrency_action(1.05) == "Buy more cryptocurrency"

        mock_prediction_rate.return_value = 0.8
        assert cryptocurrency_action(0.94) == "Sell all your cryptocurrency"

        mock_prediction_rate.return_value = 19
        assert cryptocurrency_action(20) == "Do nothing"
        mock_prediction_rate.return_value = 21
        assert cryptocurrency_action(20) == "Do nothing"


def test_cryptocurrency_action_error() -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
