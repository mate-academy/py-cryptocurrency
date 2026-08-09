from collections.abc import Callable
import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_prediction,current_rate,message",
    [
        pytest.param(110, 100, "Buy more cryptocurrency", id="110, 100, buy"),
        pytest.param(90, 100, "Sell all your cryptocurrency", id="sell"),
        pytest.param(100, 104, "Do nothing", id="100, 104, no action"),
        pytest.param(105, 100, "Do nothing", id="105, 100, no action"),
        pytest.param(95, 100, "Do nothing", id="95, 100, no action"),
        pytest.param(100, 100, "Do nothing", id="100, 100, no action")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: Callable,
        rate_prediction: int | float,
        current_rate: int | float,
        message: str) -> None:

    mock_prediction.return_value = rate_prediction

    assert cryptocurrency_action(current_rate) == message
    mock_prediction.assert_called_once_with(current_rate)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_divide_on_zero_error(mock_prediction: Callable) -> None:

    mock_prediction.return_value = 0
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
