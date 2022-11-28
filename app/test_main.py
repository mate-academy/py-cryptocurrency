from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_get_exchange_rate_prediction: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_cryptocurrency(
        mock_get_exchange_rate_prediction: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
