from unittest.mock import MagicMock, patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_get_prediction: MagicMock,
) -> None:
    mock_get_prediction.return_value = 106.0

    result = cryptocurrency_action(100.0)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mock_get_prediction: MagicMock,
) -> None:
    mock_get_prediction.return_value = 94.0

    result = cryptocurrency_action(100.0)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_within_limit(
    mock_get_prediction: MagicMock,
) -> None:
    mock_get_prediction.return_value = 102.0

    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_boundary_upper(
    mock_get_prediction: MagicMock,
) -> None:
    mock_get_prediction.return_value = 105.0

    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_boundary_lower(
    mock_get_prediction: MagicMock,
) -> None:
    mock_get_prediction.return_value = 95.0

    result = cryptocurrency_action(100.0)
    assert result == "Do nothing"
