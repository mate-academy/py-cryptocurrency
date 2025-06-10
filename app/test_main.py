from typing import Union
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 105.00, "Do nothing"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 95.00, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        mocker: pytest.MockFixture,
        current_rate: Union[int, float],
        predicted_rate: Union[int, float],
        expected: str
) -> None:
    mocker.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate
    )

    result = cryptocurrency_action(current_rate)
    assert result == expected
