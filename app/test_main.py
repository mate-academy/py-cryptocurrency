from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.mark.parametrize(
    "rate, exchange_pred, result",
    [
        (0.25, 1, "Buy more cryptocurrency"),
        (1, 0.9, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing")

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_actions_for_crypto(get_exchange,
                            rate,
                            exchange_pred,
                            result) -> None:
    get_exchange.return_value = exchange_pred
    assert(
        cryptocurrency_action(rate) == result
    )






#
# @mock.patch("app.main.random.random")
# @mock.patch("app.main.random.choice")
# def test_by_more_crypto(choice, randoms):
#     choice.return_value = "increase"
#     randoms.return_value = 0.25
#     assert (
#         cryptocurrency_action(1) == "Buy more cryptocurrency"
#     )
#     choice.return_value = "increase"
#     randoms.return_value = 1
#     assert (
#             cryptocurrency_action(2) == "Do nothing"
#     )
#     choice.return_value = "decrease"
#     randoms.return_value = 0.25
#     assert (
#             cryptocurrency_action(2) == "Sell all your cryptocurrency"
#     )
#
