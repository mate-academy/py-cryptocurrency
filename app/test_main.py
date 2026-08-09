import app.main as main
from unittest.mock import patch, MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_more_5_percent_than_course(mock_exchange: MagicMock) -> None:
    mock_exchange.return_value = 106
    result = main.cryptocurrency_action(
        100
    )
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_less_5_percent_than_course(mock_exchange: MagicMock) -> None:
    mock_exchange.return_value = 94
    result = main.cryptocurrency_action(
        100
    )
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_more_than_course_but_less_than_5(mock_exchange: MagicMock) -> None:
    mock_exchange.return_value = 103
    result = main.cryptocurrency_action(
        100
    )
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_less_than_course_but_less_than_5(mock_exchange: MagicMock) -> None:
    mock_exchange.return_value = 97
    result = main.cryptocurrency_action(
        100
    )
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_course_more_5_percent(mock_exchange: MagicMock) -> None:
    mock_exchange.return_value = 105
    result = main.cryptocurrency_action(
        100
    )
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_course_less_5_percent(mock_exchange: MagicMock) -> None:
    mock_exchange.return_value = 95
    result = main.cryptocurrency_action(
        100
    )
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_course_equal(mock_exchange: MagicMock) -> None:
    mock_exchange.return_value = 100
    result = main.cryptocurrency_action(
        100
    )
    assert result == "Do nothing"
