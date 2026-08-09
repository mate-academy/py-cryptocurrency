from unittest import mock

from app.main import cryptocurrency_action


class TestMain():

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_buy_more_with_appr_exc_rate(
            self,
            mock_get_exchange_rate_prediction: mock.MagicMock,
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.06
        assert cryptocurrency_action(1.00) == "Buy more cryptocurrency"
        mock_get_exchange_rate_prediction.assert_called_once_with(1.00)

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_sell_when_bad_rate(
            self,
            mock_get_exchange_rate_prediction: mock.MagicMock,
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.94
        assert cryptocurrency_action(1.00) == "Sell all your cryptocurrency"
        mock_get_exchange_rate_prediction.assert_called_once_with(1.00)

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_do_nothing_higher_limit(
            self,
            mock_get_exchange_rate_prediction: mock.MagicMock,
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.05
        assert cryptocurrency_action(1.00) == "Do nothing"
        mock_get_exchange_rate_prediction.assert_called_once_with(1.00)

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_do_nothing_lower_limit(
        self,
        mock_get_exchange_rate_prediction: mock.MagicMock,
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.95
        assert cryptocurrency_action(1.00) == "Do nothing"
        mock_get_exchange_rate_prediction.assert_called_once_with(1.00)
