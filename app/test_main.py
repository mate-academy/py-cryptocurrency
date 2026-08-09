from unittest import mock


from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_cryptocurrency_action_do_nothing_when0_95(
        mock_exchange_rate: float) -> None:
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction",
            return_value=1.05)
def test_cryptocurrency_action_do_nothing_when_1_05(
        mock_exchange_rate: float) -> None:
    assert cryptocurrency_action(1) == "Do nothing"

# @mock.patch("app.main.get_exchange_rate_prediction", return_value=2)
# def test_cryptocurrency_action_buy_more(mock_exchange_rate: float) -> None:
#     assert cryptocurrency_action(1) == "Buy more cryptocurrency"
#
# @mock.patch("app.main.get_exchange_rate_prediction", return_value=1)
# def test_cryptocurrency_action_sell_all(mock_exchange_rate: float) -> None:
#     assert cryptocurrency_action(2) == "Sell all your cryptocurrency"
