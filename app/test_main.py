import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mocked_prediction, expected_action",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mocked_prediction: int | float,
        expected_action: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=mocked_prediction):
        assert cryptocurrency_action(1) == expected_action
