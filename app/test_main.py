import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("curr_rate", "prediction", "result"),
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (2, 1, "Sell all your cryptocurrency"),
        (4, 4, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05,  "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_rate(
        mocked_function: mock,
        curr_rate: int | float,
        prediction: int | float,
        result: str
) -> None:
    mocked_function.return_value = prediction
    assert cryptocurrency_action(curr_rate) == result
