from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more_cryptocurraancy(
        mock_exchange_rate_prediction: mock
) -> None:
    mock_exchange_rate_prediction.return_value = 2
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all_your_cryptocurrancy(
        mock_exchange_rate_prediction: mock
) -> None:
    mock_exchange_rate_prediction.return_value = 0.5
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == ("Sell all "
                                                   "your cryptocurrency")


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mock_exchange_rate_prediction: mock
) -> None:
    mock_exchange_rate_prediction.return_value = 1.0
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_095(
        mock_exchange_rate_prediction: mock
) -> None:
    mock_exchange_rate_prediction.return_value = 0.95
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_105(
        mock_exchange_rate_prediction: mock
) -> None:
    mock_exchange_rate_prediction.return_value = 1.05
    current_rate = 1.0
    assert cryptocurrency_action(current_rate) == "Do nothing"
