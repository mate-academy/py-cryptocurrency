from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(
            100, 106, "Buy more cryptocurrency",
            id="buy_when_prediction_more_than_5_percent_higher",
        ),
        pytest.param(
            100, 94, "Sell all your cryptocurrency",
            id="sell_when_prediction_more_than_5_percent_lower",
        ),
        pytest.param(
            100, 100, "Do nothing",
            id="do_nothing_when_rate_does_not_change",
        ),
        pytest.param(
            100, 105, "Do nothing",
            id="do_nothing_when_prediction_exactly_5_percent_higher",
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="do_nothing_when_prediction_exactly_5_percent_lower",
        ),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock.MagicMock,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str,
) -> None:
    mocked_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected
    mocked_prediction.assert_called_once_with(current_rate)
