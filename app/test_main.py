from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,expected",
    [
        (100, 200, "Buy more cryptocurrency"),
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 50, "Sell all your cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 104.9, "Do nothing"),
        (100, 95.1, "Do nothing"),
    ],
    ids=[
        "should buy when prediction is much higher",
        "should buy when prediction is more than 5 percent higher",
        "should sell when prediction is much lower",
        "should sell when prediction is more than 5 percent lower",
        "should do nothing when prediction is equal to current rate",
        "should do nothing when prediction is exactly 5 percent higher",
        "should do nothing when prediction is exactly 5 percent lower",
        "should do nothing when prediction is less than 5 percent higher",
        "should do nothing when prediction is less than 5 percent lower",
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: mock.MagicMock,
    current_rate: float,
    prediction: float,
    expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected, (
        f"Should return '{expected}' when current rate is {current_rate} "
        f"and prediction is {prediction}"
    )


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_should_be_called_once_with_current_rate(
    mock_get_exchange_rate_prediction: mock.MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 100
    cryptocurrency_action(100)
    mock_get_exchange_rate_prediction.assert_called_once_with(100), (
        "Prediction should be called once with 'current_rate'"
    )
