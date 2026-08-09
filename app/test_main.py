from unittest.mock import patch, MagicMock
from app import main


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_when_prediction_more_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 106  # 6% increase

    result = main.cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency_when_prediction_less_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 94  # 6% decrease

    result = main.cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_exactly_5_percent_increase(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 105  # exactly 5%

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_exactly_5_percent_decrease(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 95  # exactly -5%

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_less_than_5_percent_change(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 102  # +2%

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"
