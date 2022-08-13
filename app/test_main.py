from unittest import mock
import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.fixture()
    def mocked_get_exchange_rate_prediction(self):
        with mock.patch("app.main.get_exchange_rate_prediction") as \
                mock_get_exchange_rate_prediction:
            yield mock_get_exchange_rate_prediction

    @pytest.mark.parametrize(
        "prediction_rate,current_rate,expected_value",
        [
            (1.1, 0.9, "Buy more cryptocurrency"),
            (0.9, 1.1, "Sell all your cryptocurrency"),
            (1, 0.99, "Do nothing"),
            (0.95, 1, "Do nothing"),
            (1.05, 1, "Do nothing"),
        ]
    )
    def test_cryptocurrency_action_when_rate_gt_1_05(
            self,
            prediction_rate,
            current_rate,
            expected_value,
            mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_value
