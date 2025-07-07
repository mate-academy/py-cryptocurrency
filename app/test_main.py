import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("value_prediction, current_value, advice", [
    (106, 100, "Buy more cryptocurrency"),
    (58, 75, "Sell all your cryptocurrency"),
    (258, 256, "Do nothing"),
    (105, 100, "Do nothing"),
    (95, 100, "Do nothing"),
])
def test_cryptocurrency_action(
        value_prediction: int,
        current_value: int,
        advice: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=value_prediction
    ):
        assert cryptocurrency_action(current_value) == advice
