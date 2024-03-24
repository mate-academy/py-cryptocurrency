from unittest.mock import patch
from pytest import mark
from app.main import cryptocurrency_action


@mark.parametrize(
    "prediction, result",
    [
        (106.0, "Buy more cryptocurrency"),
        (94.0, "Sell all your cryptocurrency"),
        (101.0, "Do nothing"),
        (105.0, "Do nothing"),
        (95.0, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
        prediction: float,
        result: str
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction", return_value=prediction
    ):
        assert cryptocurrency_action(100) == result
