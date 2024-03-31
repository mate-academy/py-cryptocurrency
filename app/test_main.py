import pytest

from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
class TestCryptocurrenceAction:

    @pytest.mark.parametrize(
        "prediction_rate, output",
        [
            pytest.param(106, "Buy more cryptocurrency"),
            pytest.param(94, "Sell all your cryptocurrency"),
            pytest.param(95, "Do nothing"),
            pytest.param(100, "Do nothing"),
            pytest.param(105, "Do nothing"),
        ],
    )
    def test_should_return_correct_result(
        self,
        mocked_get_exchange_rate_predictionn: mock.MagicMock,
        prediction_rate: int,
        output: str,
    ) -> None:
        current_rate = 100
        mocked_get_exchange_rate_predictionn.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == output

    def test_shoul_call_get_exchange_rate(
        self, mocked_get_exchange_rate_predictionn: mock.MagicMock
    ) -> None:
        current_rate = 100
        mocked_get_exchange_rate_predictionn.return_value = 100
        cryptocurrency_action(current_rate)
        mocked_get_exchange_rate_predictionn.assert_called_once_with(
            current_rate
        )
