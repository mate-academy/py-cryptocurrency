from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more_cryptocurrency(
        moked_exchange_rate_prediction: float
) -> None:
    moked_exchange_rate_prediction.return_value = 1.1
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all_your_cryptocurrency(
        moked_exchange_rate_prediction: float
) -> None:
    moked_exchange_rate_prediction.return_value = 0.9
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        moked_exchange_rate_prediction: float
) -> None:
    moked_exchange_rate_prediction.return_value = 1.02
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_not_sell(
        moked_exchange_rate_prediction: float
) -> None:
    moked_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_not_buy(
        moked_exchange_rate_prediction: float
) -> None:
    moked_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"
