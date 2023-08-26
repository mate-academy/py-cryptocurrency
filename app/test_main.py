import pytest

from unittest import mock
from unittest.mock import Mock

from app.main import cryptocurrency_action


class TestExchangePrediction:

    @pytest.fixture()
    def mocked_prediction_rate(self) -> Mock:
        with mock.patch(
            "app.main.get_exchange_rate_prediction"
        ) as mock_predict_rate:
            yield mock_predict_rate

    @pytest.mark.parametrize(
        "rate,expected",
        [
            pytest.param(
                1.1,
                "Buy more cryptocurrency",
                id="test_when_rate_higher_5%"
            ),
            pytest.param(
                0.8,
                "Sell all your cryptocurrency",
                id="test_when_rate_lower_5%"
            ),
            pytest.param(
                1.05,
                "Do nothing",
                id="test_when_rate_is_5%"
            ),
            pytest.param(
                0.95,
                "Do nothing",
                id="test_when_rate_is_minus_5%"
            ),
        ]
    )
    def test_prediction(
            self,
            rate: float,
            expected: str,
            mocked_prediction_rate: Mock
    ) -> None:
        mocked_prediction_rate.return_value = rate * 100

        actual = cryptocurrency_action(100)

        assert actual == expected
