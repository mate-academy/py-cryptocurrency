from app.main import cryptocurrency_action
import pytest
from unittest import mock


@pytest.mark.parametrize(
    "random_choice,result",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        result: str,
        random_choice: int | float,
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=random_choice):
        assert cryptocurrency_action(1) == result
# write your code here
