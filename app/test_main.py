import pytest
from unittest import mock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @pytest.mark.parametrize(
        "current_rate, predicted_rate, action",
        [
            pytest.param(
                100,
                95,
                "Do nothing",
                id="Rate prediction less then 5 percent down"
            ),
            pytest.param(
                100,
                105,
                "Do nothing",
                id="Rate prediction less then 5 percent up"
            ),
            pytest.param(
                100,
                150,
                "Buy more cryptocurrency",
                id="Rate prediction will up"
            ),
            pytest.param(
                100,
                50,
                "Sell all your cryptocurrency",
                id="Rate prediction will down"
            )
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_should_give_correct_action(
            self,
            mocked_rate_prediction,
            current_rate,
            predicted_rate,
            action
    ):
        mocked_rate_prediction.return_value = predicted_rate

        assert cryptocurrency_action(current_rate) == action
        mocked_rate_prediction.assert_called_once_with(current_rate)
