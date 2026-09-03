from unittest.mock import patch, MagicMock
import app.main as main


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_prediction_more_than_5_percent_higher(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 106
    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_when_prediction_more_than_5_percent_lower(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94
    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_difference_is_small(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 100
    assert main.cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_exact_upper_boundary(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105  # razão == 1.05 exatamente
    assert main.cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_exact_lower_boundary(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 95  # razão == 0.95 exatamente
    assert main.cryptocurrency_action(100) == "Do nothing"
