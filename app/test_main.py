from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_less_than_5_prc_change_returns_do_nothing(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 8.0

    assert cryptocurrency_action(8) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_low_prediction_returns_sell(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 7.0

    assert cryptocurrency_action(8) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_with_high_prediction_returns_buy(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 9.0

    assert cryptocurrency_action(8) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 95.0

    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 105.0

    assert cryptocurrency_action(100) == "Do nothing"
