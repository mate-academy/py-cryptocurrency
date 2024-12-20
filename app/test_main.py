import pytest
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (4, 4.24, "Buy more cryptocurrency"),
        (4, 3.76, "Sell all your cryptocurrency"),
        (4, 4.2, "Do nothing"),
        (4, 3.8, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock.MagicMock,
        current_rate: int | float,
        prediction_rate: int | float,
        result: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
