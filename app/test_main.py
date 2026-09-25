from unittest.mock import patch

from app import main


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: object) -> None:
    mock_prediction.return_value = 106

    result = main.cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: object) -> None:
    mock_prediction.return_value = 94

    result = main.cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_do_nothing_at_five_percent_lower_boundary(
    mock_prediction: object,
) -> None:
    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_do_nothing_at_five_percent_upper_boundary(
    mock_prediction: object,
) -> None:
    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"
