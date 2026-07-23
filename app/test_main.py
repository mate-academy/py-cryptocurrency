from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_equal_to_boundary(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 100
    assert cryptocurrency_action(105) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_minimal_change(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 101
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exact_5_percent_up(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exact_5_percent_down(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
