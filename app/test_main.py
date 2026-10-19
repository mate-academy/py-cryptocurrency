from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_ratio_095_should_do_nothing(
    mock_prediction: MagicMock,
) -> None:
    current_rate = 100
    mock_prediction.return_value = 95

    assert cryptocurrency_action(current_rate) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_ratio_105_should_do_nothing(
    mock_prediction: MagicMock,
) -> None:
    current_rate = 100
    mock_prediction.return_value = 105

    assert cryptocurrency_action(current_rate) == "Do nothing"
