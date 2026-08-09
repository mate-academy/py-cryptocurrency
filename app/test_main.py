import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "random_rate, expected_action",
    [
        (1.06, "Buy more cryptocurrency"),
        (1.05, "Do nothing"),
        (1.00, "Do nothing"),
        (0.95, "Do nothing"),
        (0.94, "Sell all your cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
        random_rate: float,
        expected_action: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=random_rate
    ):
        assert cryptocurrency_action(1.0) == expected_action
