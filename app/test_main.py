from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_with_rate_more_five_percent(
        mock_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 10.52
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_with_rate_less_five_percent(
        mock_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 9.4
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_without_rate(
        mock_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
