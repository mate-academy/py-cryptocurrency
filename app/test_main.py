import pytest
from typing import Union
from unittest import mock
from app.main import cryptocurrency_action


class TestExchangeRatePrediction:
    @pytest.mark.parametrize(
        "predict_rate, expected",
        [
            pytest.param(
                110,
                "Buy more cryptocurrency",
                id="Buy more cryptocurrency"
            ),
            pytest.param(
                105,
                "Do nothing",
                id="difference is not that much"
            ),
            pytest.param(
                95,
                "Do nothing",
                id="difference is not that much",
            ),
            pytest.param(
                90,
                "Sell all your cryptocurrency",
                id="Sell all your cryptocurrency"
            )
        ]
    )
    def test_cryptocurrency_action(
            self,
            predict_rate: Union[int, float],
            expected: str,
    ) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction") \
                as mocked_expected:
            mocked_expected.return_value = predict_rate
            assert cryptocurrency_action(100) == expected
            mocked_expected.assert_called_with(100)
