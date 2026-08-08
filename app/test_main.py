import pytest
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @mock.patch("app.main.get_exchange_rate_prediction")
    @pytest.mark.parametrize(
        "prediction_value,current_rate,expected_result",
        [
            (1.06, 1, "Buy more cryptocurrency"),
            (0.94, 1, "Sell all your cryptocurrency"),
            (1.05, 1, "Do nothing"),
            (0.95, 1, "Do nothing")
        ]
    )
    def test_should_return_valid_value(self,
                                       mock_prediction,
                                       prediction_value,
                                       current_rate,
                                       expected_result):

        mock_prediction.return_value = prediction_value
        assert cryptocurrency_action(current_rate) == expected_result
