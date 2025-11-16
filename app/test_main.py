from unittest.mock import patch
from app.main import cryptocurrency_action


# ---------------------------------------------------------
# Buy more if prediction > 5% above current
# ---------------------------------------------------------
@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: int) -> None:
    mock_prediction.return_value = 106  # > 105 → buy

    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


# ---------------------------------------------------------
# Sell all if prediction < 5% below current
# ---------------------------------------------------------
@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: int) -> None:
    mock_prediction.return_value = 94  # < 95 → sell

    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


# ---------------------------------------------------------
# Do nothing if prediction within ±5%
# ---------------------------------------------------------
@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_exactly_5_percent(mock_prediction: int) -> None:
    mock_prediction.return_value = 105  # exactly 5% → do nothing

    result = cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_within_range(mock_prediction: int) -> None:
    mock_prediction.return_value = 102  # within ±5% → do nothing

    result = cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_prediction: int) -> None:
    mock_prediction.return_value = 95  # exactly 5% below current
    result = cryptocurrency_action(100)
    assert result == "Do nothing", (
        "You should not sell cryptocurrency when prediction_rate/current_rate"
        " == 0.95"
    )
