from unittest import mock

import app


@mock.patch("app.main.get_exchange_rate_prediction")
def test_more_than_5_percents_higher(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    current = 100
    predicted = 110
    mock_get_exchange_rate_prediction.return_value = predicted
    assert app.main.cryptocurrency_action(current) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_exactly_5_percent_higher(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    current = 100
    predicted = 105
    mock_get_exchange_rate_prediction.return_value = predicted
    assert app.main.cryptocurrency_action(current) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_exactly_5_percent_lower(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    current = 100
    predicted = 95
    mock_get_exchange_rate_prediction.return_value = predicted
    assert app.main.cryptocurrency_action(current) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_more_than_5_percents_lower(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    current = 100
    predicted = 80
    mock_get_exchange_rate_prediction.return_value = predicted
    result = app.main.cryptocurrency_action(current)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_predicted_rate_within_5_percent_range(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    current = 100
    predicted = 99
    mock_get_exchange_rate_prediction.return_value = predicted
    assert app.main.cryptocurrency_action(current) == "Do nothing"
