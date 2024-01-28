from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.random.random")
@mock.patch("app.main.random.choice")
def test_by_more_crypto(choice, randoms):
    choice.return_value = "increase"
    randoms.return_value = 0.25
    assert (
        cryptocurrency_action(1) == "Buy more cryptocurrency"
    )
    choice.return_value = "increase"
    randoms.return_value = 1
    assert (
            cryptocurrency_action(2) == "Do nothing"
    )
    choice.return_value = "decrease"
    randoms.return_value = 0.25
    assert (
            cryptocurrency_action(2) == "Sell all your cryptocurrency"
    )

