from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_indicator_when_predicted_rate_more_than_5_percent_higher_from_current(
        mock_rate: MagicMock) -> None:
    mock_rate.return_value = 2.12
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_indicator_when_predicted_rate_more_than_5_percent_lower_from_current(
        mock_rate: MagicMock) -> None:
    mock_rate.return_value = 1.88
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_indicator_when_predicted_rate_not_so_different_from_current(
        mock_rate: MagicMock) -> None:
    mock_rate.return_value = 2
    assert cryptocurrency_action(2) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_when_difference_between_predicted_rate_and_current_is_105_percent(
        mock_rate: MagicMock) -> None:
    mock_rate.return_value = 2.1
    assert cryptocurrency_action(2) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_when_difference_between_predicted_rate_and_current_is_95_percent(
        mock_rate: MagicMock) -> None:
    mock_rate.return_value = 1.9
    assert cryptocurrency_action(2) == "Do nothing"
