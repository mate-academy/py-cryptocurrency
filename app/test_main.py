from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = current_rate * 1.06
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = current_rate * 0.94
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.side_effect = \
        [current_rate * 0.96, current_rate * 1.04]

    result1 = cryptocurrency_action(current_rate)
    assert result1 == "Do nothing"

    result2 = cryptocurrency_action(current_rate)
    assert result2 == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_boundary(
        mock_get_exchange_rate_prediction: MagicMock
) -> None:
    current_rate = 100
    mock_get_exchange_rate_prediction.side_effect = \
        [current_rate * 0.96, current_rate * 1.04]

    result1 = cryptocurrency_action(current_rate)
    assert result1 == "Do nothing"
    result2 = cryptocurrency_action(current_rate)
    assert result2 == "Do nothing"
