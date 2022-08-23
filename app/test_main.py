import pytest
from unittest import mock
from app.main import cryptocurrency_action


class Test():

    @mock.patch("app.main.get_exchange_rate_prediction")
    @pytest.mark.parametrize(
        "prediction_rate, current_rate, expected_result", [
            (1.06, 1, "Buy more cryptocurrency"),
            (0.94, 1, "Sell all your cryptocurrency"),
            (1.05, 1, "Do nothing"),
            (0.95, 1, "Do nothing")
        ]
    )
    def test_crypto(self, mock_fee,
                    prediction_rate,
                    current_rate,
                    expected_result):
        mock_fee.return_value = prediction_rate

        assert cryptocurrency_action(current_rate) == expected_result
