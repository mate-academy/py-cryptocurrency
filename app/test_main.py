from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_when_rate_higher_5(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 120
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_sell_all_when_rate_higher_5(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_rate_more(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_rate_less(
        mock_get_exchange_rate_prediction: mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
