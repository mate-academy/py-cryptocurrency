import pytest
from unittest.mock import patch, Mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,"
    "exchange_rate_prediction_return_value,"
    "result",
    [
        pytest.param(
            1, 1.06, "Buy more cryptocurrency",
            id="should return 'Buy more cryptocurrency' "
               "when prediction_rate / current_rate > 1.05"
        ),
        pytest.param(
            1, 0.94, "Sell all your cryptocurrency",
            id="should return 'Sell all your cryptocurrency' "
               "when prediction_rate / current_rate < 0.95"
        ),
        pytest.param(
            1, 1, "Do nothing",
            id="should return 'Do nothing' "
               "when difference is not that much"
        ),
        pytest.param(
            1, 0.95, "Do nothing",
            id="should return 'Do nothing' "
               "when difference is not that much"
        ),
        pytest.param(
            1, 1.05, "Do nothing",
            id="should return 'Do nothing' "
               "when difference is not that much"
        ),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: Mock,
        current_rate: int | float,
        exchange_rate_prediction_return_value: int | float,
        result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = (
        exchange_rate_prediction_return_value
    )
    assert cryptocurrency_action(current_rate) == result

    mocked_get_exchange_rate_prediction.assert_called_once_with(current_rate)
