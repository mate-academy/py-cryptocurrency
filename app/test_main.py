from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_more_five_persent(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 27
    cryptocurrency_action(25)
    assert cryptocurrency_action(25) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_not_more_five_persent(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 23
    cryptocurrency_action(26)
    assert cryptocurrency_action(26) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_when_rate_is_not_then_mach(
        mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 25.65
    cryptocurrency_action(27)
    assert cryptocurrency_action(27) == "Do nothing"
    mock_rate_prediction.return_value = 28.35
    cryptocurrency_action(27)
    assert cryptocurrency_action(27) == "Do nothing"
