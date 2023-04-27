from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.1 * 100
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.93 * 100
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05 * 100
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_dont_sell_all(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95 * 100
    assert cryptocurrency_action(100) == "Do nothing"
