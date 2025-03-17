from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_prediction: int) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing", (
        "You should not buy cryptocurrency when prediction_rate "
        "/ current_rate == 1.05"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_prediction: int) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing", (
        "You should not sell cryptocurrency when prediction_rate "
        "/ current_rate == 0.95"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_prediction: int) -> None:
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

    mock_prediction.return_value = 104
    assert cryptocurrency_action(100) == "Do nothing"

    mock_prediction.return_value = 96
    assert cryptocurrency_action(100) == "Do nothing"

    mock_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
