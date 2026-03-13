from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_buy_more(
    mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 2

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_sell_all(
    mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 0.8

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_do_nothing(
    mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_should_return_do_nothing_with(
    mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"
