from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "get_exchange_return,current_rate_parametrize,expected_return",
    [
        (100, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (94, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency")
    ],
    ids=["prediction_rate == current_rate, do nothing",
         "prediction_rate 5% < than current_rate, do nothing",
         "prediction_rate 6% < than current_rate, sell all",
         "prediction_rate 5% > than current_rate, do nothing",
         "prediction_rate 6% > than current_rate, buy more"]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction,
                               get_exchange_return,
                               current_rate_parametrize,
                               expected_return):

    mock_get_exchange_rate_prediction.return_value = get_exchange_return

    result = cryptocurrency_action(current_rate_parametrize)
    mock_get_exchange_rate_prediction.assert_called_once_with(
        current_rate_parametrize
    )

    assert result == expected_return
