import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency")
    ],
    ids=[
        "Buy more cryptocurrency when prediction 5%+",
        "Do nothing when prediction +5%",
        "Do nothing when prediction -5%",
        "Sell all your cryptocurrency when prediction lower than -5%"
    ]
)
def test_cryptocurrency_action(
    current_rate: int | float,
    prediction_rate: int | float,
    expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as predict:
        predict.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected
