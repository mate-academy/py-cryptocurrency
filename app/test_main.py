import pytest

from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current, prediction, expected",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.9, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(mocked: mock,
                               current: int,
                               prediction: float,
                               expected: str) -> None:
    mocked.return_value = prediction
    assert cryptocurrency_action(current) == expected
