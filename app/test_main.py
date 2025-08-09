from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_current_rate_is_higher(
        mock_prediction: mock.MagicMock()) -> None:
    mock_prediction.return_value = 1500
    assert cryptocurrency_action(1000) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_current_rate_is_lower(
        mock_prediction: mock.MagicMock()) -> None:
    mock_prediction.return_value = 500
    assert cryptocurrency_action(1000) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_current_rate_is_the_same(
        mock_prediction: mock.MagicMock()) -> None:
    mock_prediction.return_value = 1090
    assert cryptocurrency_action(1050) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_current_rate_is_almost_higher(
        mock_prediction: mock.MagicMock()) -> None:
    mock_prediction.return_value = 950
    assert cryptocurrency_action(1000) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_current_rate_is_almost_lower(
        mock_prediction: mock.MagicMock()) -> None:
    mock_prediction.return_value = 1050
    assert cryptocurrency_action(1000) == "Do nothing"
