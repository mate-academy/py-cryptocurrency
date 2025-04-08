from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_prediction_rate_going_up(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 200.05

    result = cryptocurrency_action(10)

    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_prediction_rate_going_down(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 5.02

    result = cryptocurrency_action(10)

    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_when_prediction_rate_is_small_different_in_lower_point(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 9.5

    result = cryptocurrency_action(10)

    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_rating_is_small_difference_in_highest_point(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 10.5

    result = cryptocurrency_action(10)

    assert result == "Do nothing"
