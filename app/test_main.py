import pytest

from unittest import mock

from app.main import cryptocurrency_action


class TestCorrectResults:
    @pytest.mark.parametrize(
        "exchange_rate,prediction_rate,expected_results",
        [
            (100, 106, "Buy more cryptocurrency"),
            (100, 105, "Do nothing"),
            (100, 95, "Do nothing"),
            (100, 94, "Sell all your cryptocurrency"),
        ],
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
        self,
        mock_get_exchange_rate_prediction: callable,
        exchange_rate: int,
        prediction_rate: int,
        expected_results: str,
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(exchange_rate) == expected_results

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_call_get_exchange_rate_prediction(
        self,
        mock_get_exchange_rate_prediction: callable,
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1
        cryptocurrency_action(1)
        mock_get_exchange_rate_prediction.assert_called_once()
