import pytest
from unittest.mock import patch, MagicMock
from typing import Union
from app import main


class TestCryptoCurrencyAction:
    @pytest.mark.parametrize(
        "current_rate,mocked_prediction,expected_result",
        [
            (100, 110, "Buy more cryptocurrency"),
            (100, 90, "Sell all your cryptocurrency"),
            (100, 100, "Do nothing"),
            (100, 105, "Do nothing"),
            (100, 95, "Do nothing"),
        ],
        ids=[
            "Need buying more",
            "Need sell",
            "Nothing",
            "Nothing",
            "Nothing",
        ]
    )
    @patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
        self,
        mocked_function: MagicMock,
        current_rate: Union[int, float],
        mocked_prediction: Union[int, float],
        expected_result: str
    ) -> None:
        mocked_function.return_value = mocked_prediction
        assert main.cryptocurrency_action(current_rate) == expected_result
