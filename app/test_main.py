from unittest import mock, TestCase

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):
    def setUp(self) -> None:
        self.current_rate = 1

    @mock.patch(
        "app.main.get_exchange_rate_prediction",
        side_effect=lambda x: 1.06
    )
    def test_buy_more_edge_case(self,
                                mocked_prediction: float
                                ) -> None:

        assert cryptocurrency_action(self.current_rate) \
               == "Buy more cryptocurrency"

    @mock.patch(
        "app.main.get_exchange_rate_prediction",
        side_effect=lambda x: 0.94
    )
    def test_sell_all_edge_case(self,
                                mocked_prediction: float
                                ) -> None:

        assert (
            cryptocurrency_action(self.current_rate)
            == "Sell all your cryptocurrency"
        )

    @mock.patch(
        "app.main.get_exchange_rate_prediction",
        side_effect=lambda x: 1.05
    )
    def test_do_nothing_left_edge_case(self,
                                       mocked_prediction: float
                                       ) -> None:

        assert cryptocurrency_action(self.current_rate) == "Do nothing"

    @mock.patch(
        "app.main.get_exchange_rate_prediction",
        side_effect=lambda x: 0.95
    )
    def test_do_nothing_right_edge_case(self,
                                        mocked_prediction: float
                                        ) -> None:

        assert cryptocurrency_action(self.current_rate) == "Do nothing"
