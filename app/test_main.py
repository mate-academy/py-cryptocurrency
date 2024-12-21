import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestClass:
    @patch("app.main.get_exchange_rate_prediction")
    def test_first_func(mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 110
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"
