from pytest import mark
from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@mark.parametrize(
    "prediction_rate,result",
    [
        (1.05, "Do nothing"),
        (1.06, "Buy more cryptocurrency"),
        (0.95, "Do nothing"),
        (0.94, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        mocked_prediction: object,
        prediction_rate: int | float,
        result: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(1) == result
