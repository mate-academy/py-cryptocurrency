from app.main import cryptocurrency_action

from pytest import mark

from unittest.mock import patch


@mark.parametrize(
    "prediction_rate, expected_value",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    ]
)
def test_cryptocurrency_action(prediction_rate: int | float,
                               expected_value: str) -> None:
    with (patch("app.main.get_exchange_rate_prediction") as random):
        random.return_value = prediction_rate
        assert cryptocurrency_action(1) == expected_value
