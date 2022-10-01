import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate():
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mock_exchange:
        yield mock_exchange


class TestCryptocurrency:
    @pytest.mark.parametrize(
        "current_rate, prediction_rate, result",
        [
            pytest.param(
                10,
                10,
                "Do nothing",
                id="current rate equal prediction_rate"),
            pytest.param(
                10,
                10.5,
                "Do nothing",
                id="max limit for do nothing"),
            pytest.param(
                10,
                9.5,
                "Do nothing",
                id="min limit for do nothing with round"),
            pytest.param(
                10,
                10.56,
                "Buy more cryptocurrency",
                id="min limit for buy"),
            pytest.param(
                0.01,
                1000,
                "Buy more cryptocurrency",
                id="big value for buy"),
            pytest.param(
                10,
                9.49,
                "Sell all your cryptocurrency",
                id="max limit for sell"),
            pytest.param(
                10,
                0,
                "Sell all your cryptocurrency",
                id="min limit for sell")
        ]
    )
    def test_the_same_values(
            self,
            mocked_exchange_rate,
            current_rate,
            prediction_rate,
            result
    ):
        mocked_exchange_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result

    @pytest.mark.parametrize(
        "current_rate, prediction_rate, expected_error",
        [
            pytest.param(
                0,
                100,
                ZeroDivisionError,
                id="Zero division error"
            ),
            pytest.param(
                10,
                None,
                TypeError,
                id="prediction_rate is None"
            ),
            pytest.param(
                None,
                10,
                TypeError,
                id="current_rate is None"
            ),
            pytest.param(
                "",
                10,
                TypeError,
                id="prediction_rate is string"
            )
        ]
    )
    def test_errors(
            self,
            mocked_exchange_rate,
            current_rate,
            prediction_rate,
            expected_error
    ):
        mocked_exchange_rate.return_value = prediction_rate
        with pytest.raises(expected_error):
            cryptocurrency_action(current_rate)
