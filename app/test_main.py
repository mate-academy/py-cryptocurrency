from unittest import mock
import pytest
from app.main import cryptocurrency_action


class TestCryptoCurrencyAction:
    @pytest.mark.parametrize("current_rate, predicted_rate, expected_action", [
        (100, 110, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 103, "Do nothing"),
        (100, 97, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ])
    def test_cryptocurrency_action(self,
                                   current_rate: int,
                                   predicted_rate: int,
                                   expected_action: str) -> None:
        with (mock.patch("app.main.get_exchange_rate_prediction")
              as mock_prediction):
            mock_prediction.return_value = predicted_rate
            result = cryptocurrency_action(current_rate)
            assert result == expected_action
            mock_prediction.assert_called_once_with(current_rate)
