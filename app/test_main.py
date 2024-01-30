from app.main import cryptocurrency_action

from unittest import mock


def test_should_return_noting_if_result_less_then_0_95() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=0.95):
        assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_noting_if_result_less_than_1_05() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=1.05):
        assert cryptocurrency_action(1) == "Do nothing"

# def test_third():
#     with mock.patch("app.main.get_exchange_rate_prediction", return_value=5):
#         assert cryptocurrency_action(2.5) == "Buy more cryptocurrency"
#
#
# def test_fourth():
#     with mock.patch("app.main.get_exchange_rate_prediction", return_value=1):
#         assert cryptocurrency_action(2) == "Sell all your cryptocurrency"
