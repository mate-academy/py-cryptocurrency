import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_prediction_function_has_called(
        mock_rate_prediction: callable
) -> None:
    mock_rate_prediction.return_value = 10
    cryptocurrency_action(10)
    mock_rate_prediction.assert_called_once()


@pytest.mark.parametrize(
    "prediction_value,action_value",
    [
        pytest.param(
            1.06,
            "Buy more cryptocurrency",
            id="Should buy more if predict is bigger on 1.06"
        ),
        pytest.param(
            1.05,
            "Do nothing",
            id="Should do nothing if predict is bigger on 1.05"
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="Should do nothing if predict is lower on 0.95"
        ),
        pytest.param(
            0.94,
            "Sell all your cryptocurrency",
            id="Should sell all if predict is lower on 0.94"
        ),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_return_value(
        mock_rate_prediction: callable,
        prediction_value: float,
        action_value: str
) -> None:
    mock_rate_prediction.return_value = prediction_value
    assert cryptocurrency_action(1) == action_value
