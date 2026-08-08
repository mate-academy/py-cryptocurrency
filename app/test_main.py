import pytest
from app.main import cryptocurrency_action
from unittest.mock import MagicMock, patch
from typing import Union


@pytest.mark.parametrize(
    "current_rate, predicted_rate, result",
    [
        (60, 100, "Buy more cryptocurrency"),
        (512, 537.6, "Do nothing"),
        (158, 162, "Do nothing"),
        (333, 333, "Do nothing"),
        (10700, 10637, "Do nothing"),
        (456.78, 433.941, "Do nothing"),
        (200, 98, "Sell all your cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_for_method(mocked_predict: MagicMock,
                    current_rate: Union[int, float],
                    predicted_rate: Union[int, float],
                    result: str) -> None:
    mocked_predict.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == result


def test_zero_division_error() -> None:
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)
