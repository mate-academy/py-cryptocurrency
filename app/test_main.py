from unittest import mock

import pytest

from app.main import cryptocurrency_action


use_cases = [
    (3, 2, "Buy more cryptocurrency"),
    (1, 2, "Sell all your cryptocurrency"),
    (0.95, 1, "Do nothing"),
    (1.05, 1, "Do nothing"),
]

ids = [
    "cryptocurrency action: "
    "buy when ration is bigger then 1.05",
    "cryptocurrency action: "
    "sell when ration is less then 0.95",
    "cryptocurrency action: "
    "do nothing when ration is 0.95",
    "cryptocurrency action: "
    "do nothing when ration is 1.05"
]


@pytest.mark.parametrize(
    "predicted_value,current_rate,expected",
    use_cases,
    ids=ids
)
def test_cryptocurrency_action(
        predicted_value: int | float,
        current_rate: int | float,
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as prediction:
        prediction.return_value = predicted_value
        assert cryptocurrency_action(current_rate) == expected
