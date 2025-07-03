import pytest
from unittest import mock
from .main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exception",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (105, "Do nothing"),
        (95, "Do nothing"),
        (101, "Do nothing")
    ]
)

def test_cryptocurrency(
        current_rate: int | float,
        exception: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=current_rate
):
        result = cryptocurrency_action(100)
        assert result == exception
