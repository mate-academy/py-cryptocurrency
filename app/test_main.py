from unittest import mock

from app.main import cryptocurrency_action


class TestCryptocuracyAction():

    @mock.patch("app.main.get_exchange_rate_prediction",
                return_value=150)
    def test_cryptocurrency_action_buy_more(
            self,
            mock_get_exchange_rate_prediction: mock
    ) -> None:
        current_rate = 100
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"

    @mock.patch("app.main.get_exchange_rate_prediction",
                return_value=50)
    def test_cryptocurrency_action_sell_all(
            self,
            mock_get_exchange_rate_prediction: mock
    ) -> None:
        current_rate = 100
        assert cryptocurrency_action(current_rate) == ("Sell all your "
                                                       "cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction",
                return_value=105)
    def test_cryptocurrency_action_do_nothing_when_up(
            self,
            mock_get_exchange_rate_prediction: mock
    ) -> None:
        current_rate = 100
        assert cryptocurrency_action(current_rate) == ("Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction",
                return_value=95)
    def test_cryptocurrency_action_do_nothing_when_down(
            self,
            mock_get_exchange_rate_prediction: mock
    ) -> None:
        current_rate = 100
        assert cryptocurrency_action(current_rate) == ("Do nothing")
