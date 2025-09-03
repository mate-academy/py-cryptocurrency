import pytest
from unittest import mock
from unittest.mock import MagicMock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mock_prediction_rate, expected",
    [
        (1, 1.051, "Buy more cryptocurrency"),
        (1, 0.949, "Sell all your cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100.5, 103.5, "Do nothing"),
        (0, 1.0, ZeroDivisionError)
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_exchange_rate_prediction: MagicMock,
    current_rate: Union[float, int],
    mock_prediction_rate: Union[float, int],
    expected: Union[str, type],
) -> None:
    mock_exchange_rate_prediction.return_value = mock_prediction_rate

    if expected == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            cryptocurrency_action(current_rate)
    else:
        assert cryptocurrency_action(current_rate) == expected
