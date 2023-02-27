import pytest

from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


class TestCryptoCurrencyAction:
    @pytest.mark.parametrize(
        "current_rate,prediction_rate,expected_action",
        [
            (100, 110, "Buy more cryptocurrency"),
            (100, 90, "Sell all your cryptocurrency"),
            (100, 100, "Do nothing")
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction: object,
            current_rate: Union[int, float],
            prediction_rate: Union[int, float],
            expected_action: str
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_action

    def test_cryptocurrency_action_invalid_rate(self) -> None:
        with pytest.raises(TypeError):
            cryptocurrency_action("invalid_rate")
