from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_when_predicted_rate_is_significantly_higher(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105.1

    result: str = cryptocurrency_action(100.0)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_when_predicted_rate_is_significantly_lower(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94.9

    result: str = cryptocurrency_action(100.0)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_predicted_rate_change_is_within_boundaries(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105.0
    assert cryptocurrency_action(100.0) == "Do nothing"

    mock_prediction.return_value = 95.0
    assert cryptocurrency_action(100.0) == "Do nothing"

    mock_prediction.return_value = 100.0
    assert cryptocurrency_action(100.0) == "Do nothing"
