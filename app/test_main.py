from typing import Union
import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptoAction:
    @pytest.mark.parametrize(
        "current_rate, prediction, expected_action",
        [
            (100, 105.1, "Buy more cryptocurrency"),
            (100, 106, "Buy more cryptocurrency"),
            (100, 94.9, "Sell all your cryptocurrency"),
            (100, 94, "Sell all your cryptocurrency"),
            (100, 104, "Do nothing"),
            (100, 105, "Do nothing"),
            (100, 95, "Do nothing"),
            (100, 96, "Do nothing"),
            (100, 100, "Do nothing"),
            (10400, 10000, "Do nothing"),
        ]
    )
    def test_cryptocurrency_action(
            self,
            prediction: Union[int, float],
            current_rate: Union[int, float],
            expected_action: str
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = prediction
            result = cryptocurrency_action(current_rate)
            assert result == expected_action
            mock_prediction.assert_called_once_with(current_rate)
