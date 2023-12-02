import pytest
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @staticmethod
    @pytest.fixture
    def mocked_get_exchange_rate_prediction():
        with mock.patch("app.main.get_exchange_rate_prediction") as get_exchange_rate_prediction:
            yield get_exchange_rate_prediction

    def test_get_exchange_rate_prediction_called_with(self, mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = 74
        cryptocurrency_action(52)
        mocked_get_exchange_rate_prediction.assert_called_once_with(52)

    @pytest.mark.parametrize(
        "predictable_rate,current_rate,result",
        [
            (75 * 1.06, 75, "Buy more cryptocurrency"),
            (48 * 0.94, 48, "Sell all your cryptocurrency"),
            (39 * 1.03, 39, "Do nothing"),
            (39 * 1.05, 39, "Do nothing"),
            (39 * 0.95, 39, "Do nothing"),
        ]
    )
    def test_cryptocurrency_action(
            self,
            predictable_rate,
            current_rate,
            result,
            mocked_get_exchange_rate_prediction
            ):
        mocked_get_exchange_rate_prediction.return_value = predictable_rate
        assert cryptocurrency_action(current_rate) == result
