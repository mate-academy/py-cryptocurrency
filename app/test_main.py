from unittest import mock
import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "prediction_rate,current_rate,expected_result",
        [
            pytest.param(
                1.05, 1,
                "Do nothing"
            ),
            pytest.param(
                0.95, 1,
                "Do nothing"
            ),
            pytest.param(
                0.95, 1.05,
                "Sell all your cryptocurrency"
            ),
            pytest.param(
                1.05, 0.95,
                "Buy more cryptocurrency"
            ),
        ]
    )
    def test_should_return_correct_string(
            self,
            current_rate: int | float,
            prediction_rate: int | float,
            expected_result: str
    ) -> None:
        with (
            mock.patch("app.main.get_exchange_rate_prediction")
            as mocked_prediction_rate
        ):
            mocked_prediction_rate.return_value = prediction_rate
            assert cryptocurrency_action(current_rate) == expected_result
