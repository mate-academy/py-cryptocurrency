from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_when_rate_more_than_5_percent_higher(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 106.0
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_when_rate_more_than_5_percent_lower(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94.0
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_within_5_percent_higher(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_within_5_percent_lower(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_equal(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 100.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_at_exact_boundary(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105.01
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_at_exact_boundary(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94.99
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_called_with_current_rate(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 100.0
    cryptocurrency_action(200)
    mock_prediction.assert_called_once_with(200)
