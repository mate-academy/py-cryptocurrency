from unittest.mock import patch
from unittest.mock import MagicMock

import app.main


@patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_rate_more_than_5_percent_higher(
    mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 106

    assert app.main.cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_if_predicted_rate_more_than_5_percent_lower(
    mocked_prediction: MagicMock
) -> None:
    mocked_prediction.return_value = 94

    assert (
        app.main.cryptocurrency_action(100)
        == "Sell all your cryptocurrency"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_small_difference_lower(mocked_prediction: MagicMock) -> None:
    mocked_prediction.return_value = 95

    assert app.main.cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_small_difference_higher(mocked_prediction: MagicMock) -> None:
    mocked_prediction.return_value = 105

    assert app.main.cryptocurrency_action(100) == "Do nothing"
