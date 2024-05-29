import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, advice",
    [
        (94, 100, "Sell all your cryptocurrency"),
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency"),
    ],
    ids=[
        "Boundary value of selling",
        "Min boundary value of do nothing",
        "Max boundary value of do nothing",
        "Boundary value of buy more",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        rate_mocked_f: mock.Mock,
        prediction_rate: int | float,
        current_rate: int | float,
        advice: str
) -> None:
    rate_mocked_f.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == advice
