from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 106.0

    result = cryptocurrency_action(100.0)

    assert result == "Buy more cryptocurrency"
    mock_get_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 94.0

    result = cryptocurrency_action(100.0)

    assert result == "Sell all your cryptocurrency"
    mock_get_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_slight_increase(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 103.0

    result = cryptocurrency_action(100.0)

    assert result == "Do nothing"
    mock_get_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_slight_decrease(
        mock_get_prediction: MagicMock
) -> None:
    mock_get_prediction.return_value = 98.0

    result = cryptocurrency_action(100.0)

    assert result == "Do nothing"
    mock_get_prediction.assert_called_once()
