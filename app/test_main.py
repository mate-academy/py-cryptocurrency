from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(
        mock_get_rate_prediction: MagicMock
) -> None:
    mock_get_rate_prediction.return_value = 110
    expected_value = "Buy more cryptocurrency"

    assert cryptocurrency_action(100) == expected_value


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(
        mock_get_rate_prediction: MagicMock
) -> None:
    mock_get_rate_prediction.return_value = 94
    expected_value = "Sell all your cryptocurrency"

    assert cryptocurrency_action(100) == expected_value


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_hold_lower_limit(
        mock_get_rate_prediction: MagicMock
) -> None:
    mock_get_rate_prediction.return_value = 95
    expected_value = "Do nothing"

    assert cryptocurrency_action(100) == expected_value


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_hold_upper_limit(
        mock_get_rate_prediction: MagicMock
) -> None:
    mock_get_rate_prediction.return_value = 105
    expected_value = "Do nothing"

    assert cryptocurrency_action(100) == expected_value
