from unittest import mock
from app.main import cryptocurrency_action


# @mock.patch("app.main.get_exchange_rate_prediction",
#             return_value=110)
# def test_110_should_buy_more_cryptocurrency(
#         mocked_prediction: mock.Mock) -> None:
#     result = cryptocurrency_action(100)
#     assert result == "Buy more cryptocurrency"
#
#
# @mock.patch("app.main.get_exchange_rate_prediction",
#             return_value=90)
# def test_90_should_sell_all_you_cryptocurrency(
#         mocked_prediction: mock.Mock) -> None:
#     result = cryptocurrency_action(100)
#     assert result == "Sell all your cryptocurrency"
#
#
# @mock.patch("app.main.get_exchange_rate_prediction",
#             return_value=100)
# def test_100_should_do_nothing(
#         mocked_prediction: mock.Mock) -> None:
#     result = cryptocurrency_action(100)
#     assert result == "Do nothing"

@mock.patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_rate_105_percent_do_nothing(mocked_prediction: mock.Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_rate_95_percent_do_nothing(mocked_prediction: mock.Mock) -> None:
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"
