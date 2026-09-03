from unittest import mock

from app import main


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_more_than_5_percent(mock_prediction: mock.Mock) -> None:
    mock_prediction.return_value = 106

    result = main.cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_exactly_5_percent_higher(
    mock_prediction: mock.Mock,
) -> None:
    mock_prediction.return_value = 105

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_within_5_percent(mock_prediction: mock.Mock) -> None:
    mock_prediction.return_value = 102

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_exactly_5_percent_lower(
    mock_prediction: mock.Mock,
) -> None:
    mock_prediction.return_value = 95

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_less_than_5_percent(mock_prediction: mock.Mock) -> None:
    mock_prediction.return_value = 94

    result = main.cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"
