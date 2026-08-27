from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_when_rate_increases_more_than_5_percent(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 105.01
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_increases_exactly_5_percent(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency_when_rate_decreases_more_than_5_percent(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 94.99
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_decreases_exactly_5_percent(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_does_not_change(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
