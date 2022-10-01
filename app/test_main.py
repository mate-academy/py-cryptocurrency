from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCrypto:
    @mock.patch("app.main.get_exchange_rate_prediction")
    @pytest.mark.parametrize(
        "prediction_rate, current_rate, expected_result",
        [
            (1.06, 1, "Buy more cryptocurrency"),
            (0.94, 1, "Sell all your cryptocurrency"),
            (1.05, 1, "Do nothing"),
            (0.95, 1, "Do nothing")
        ]
    )
    def test_should_return_expected_value(self,
                                          mocked_prediction,
                                          prediction_rate,
                                          current_rate,
                                          expected_result):
        mocked_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
