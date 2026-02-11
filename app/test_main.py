from unittest import mock

import app.main as main


@mock.patch("app.main.get_exchange_rate_prediction")
class TestCryptoMock:
    def test_should_buy_cryptocurrency(
        self, mock_prediction: mock.Mock
    ) -> None:
        current_rate = 100
        mock_prediction.return_value = 106
        result = main.cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"

    def test_should_sell_cryptocurrency(
        self, mock_prediction: mock.Mock
    ) -> None:
        current_rate = 100
        mock_prediction.return_value = 94
        result = main.cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"

    def test_should_hold_cryptocurrency(
        self, mock_prediction: mock.Mock
    ) -> None:
        current_rate = 100
        mock_prediction.return_value = 105
        result = main.cryptocurrency_action(current_rate)
        assert result == "Do nothing"

    def test_should_hold_if_exactly_5_percent(
        self, mock_prediction: mock.Mock
    ) -> None:
        current_rate = 100
        mock_prediction.return_value = 95
        result = main.cryptocurrency_action(current_rate)
        assert result == "Do nothing"
