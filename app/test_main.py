import pytest
from unittest.mock import Mock, patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,result",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 96, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: Mock,
        current_rate: int | float,
        prediction: int | float,
        result: str
) -> None:
    mocked_prediction.return_value = prediction

    assert cryptocurrency_action(current_rate) == result

    mocked_prediction.assert_called_once_with(current_rate)
