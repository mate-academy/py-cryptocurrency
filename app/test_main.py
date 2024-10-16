from app.main import cryptocurrency_action
from unittest import mock


CURRENT_RATE = 1.01


@mock.patch("app.get_exchenge_rate_prediction")
def test_cryptocurrency_action_buy_more(
    mocked_get_exchenge_rate_prediction: object
) -> None:
    mocked_get_exchenge_rate_prediction.return_value = 1.25
    assert cryptocurrency_action(CURRENT_RATE) == "Buy more cryptocurrency"


@mock.patch("app.get_exchenge_rate_prediction")
def test_cryptocurrency_action_sell_all(
    mocked_get_exchenge_rate_prediction: object
) -> None:
    mocked_get_exchenge_rate_prediction.return_value = 0.95
    assert (
        cryptocurrency_action(CURRENT_RATE) == "Sell all your cryptocurrency"
    )


@mock.patch("app.get_exchenge_rate_prediction")
def test_cryptocurrency_action_do_nothing(
    mocked_get_exchenge_rate_prediction: object
) -> None:
    mocked_get_exchenge_rate_prediction.return_value = 1.01
    assert cryptocurrency_action(CURRENT_RATE) == "Do nothing"
