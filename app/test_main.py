import pytest
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptoCurrencyAction:
    @pytest.mark.parametrize(
        "exchange_rate,prediction_rate, result",
        [
            pytest.param(
                100,
                105,
                "Do nothing",
                id="increase by 5%"
            ),
            pytest.param(
                100,
                106,
                "Buy more cryptocurrency",
                id="increase more then 5%"
            ),
            pytest.param(
                100,
                104,
                "Do nothing",
                id="increase less then 5%"
            ),
            pytest.param(
                100,
                95,
                "Do nothing",
                id="decrease by 5%"
            ),
            pytest.param(
                100,
                94,
                "Sell all your cryptocurrency",
                id="decrease more then 5%"
            ),
            pytest.param(
                100,
                98,
                "Do nothing",
                id="decrease less then 5%"
            ),

        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mocked_rate_prediction,
            exchange_rate,
            prediction_rate,
            result):
        mocked_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(exchange_rate) == result
