from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (200, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ],
    ids=[
        "Prediction_rate > 1.05, buy more!",
        "Prediction_rate < 0.95, sell now!!!",
        "More then 1.0 < prediction_rate <= 1.05",
        "Less then 0.95 <= prediction_rate < 1.0",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock.MagicMock,
        prediction_rate: float,
        current_rate: float,
        result: str
) -> None:
    mocked_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
