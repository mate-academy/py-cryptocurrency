from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_increases_more_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    current_rate = 100
    mock_prediction.return_value = 110

    number = cryptocurrency_action(current_rate)
    assert number == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_decreases_more_than_5_percent(
        mock_prediction: MagicMock,
) -> None:
    current_rate = 100
    mock_prediction.return_value = 90

    new_number = cryptocurrency_action(current_rate)
    assert new_number == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_change_is_small(
    mock_prediction: MagicMock,
) -> None:
    current_rate = 100
    mock_prediction.return_value = 100

    numbers = cryptocurrency_action(current_rate)
    assert numbers == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_exacly_105_percent(
    mock_prediction: MagicMock,
) -> None:
    current_rate = 100
    mock_prediction.return_value = 105

    new_numbers = cryptocurrency_action(current_rate)
    assert new_numbers == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_exacly_95_percent(
    mock_prediction: MagicMock,
) -> None:
    current_rate = 100
    mock_prediction.return_value = 95

    num = cryptocurrency_action(current_rate)
    assert num == "Do nothing"
