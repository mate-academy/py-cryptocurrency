from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_when_prediction_is_higher_than_five_percent(
    mock_prediction: Mock
) -> None:
    # Ustawiamy przewidywaną cenę na 106% ceny obecnej (100 * 1.06 = 106)
    mock_prediction.return_value = 106.0
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_when_prediction_is_lower_than_five_percent(
    mock_prediction: Mock
) -> None:
    # Ustawiamy przewidywaną cenę na 94% ceny obecnej (100 * 0.94 = 94)
    mock_prediction.return_value = 94.0
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_difference_is_small(
    mock_prediction: Mock
) -> None:
    # Ustawiamy przewidywaną cenę na 102% ceny obecnej (100 * 1.02 = 102)
    mock_prediction.return_value = 102.0
    assert cryptocurrency_action(100) == "Do nothing"
