import pytest

from unittest import mock
from typing import Union, Type

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "current_rate, exchange, expected_result",
        [
            (4.3, 6.25, "Buy more cryptocurrency"),  # more than 1.05
            (1, 0.96, "Do nothing"),  # between 0.95 and 1.05
            (3, 0.80, "Sell all your cryptocurrency"),  # less than 0.95
            (1, 1.05, "Do nothing"),  # exactly 1.05
            (1, 0.95, "Do nothing")  # exactly 0.95
        ],
        ids=["more than 1.05",
             "between 0.95 and 1.05",
             "less than 0.95",
             "exactly 1.05",
             "exactly 0.95"
             ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_result(
            self,
            mocked_get_exchange_rate_prediction: float,
            current_rate: Union[int, float],
            exchange: float,
            expected_result: str
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = exchange
        assert cryptocurrency_action(current_rate) == expected_result


class TestExpectedError:
    @pytest.mark.parametrize(
        "current_rate, expected_error",
        [
            pytest.param(
                "5",
                TypeError,
                id="should raise TypeError if current_rate is not int"
            ),
        ]
    )
    def test_raising_correctly(
            self,
            current_rate: int,
            expected_error: Type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            cryptocurrency_action(current_rate)
