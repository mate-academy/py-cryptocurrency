import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current, predicted, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: mock,
        current: int,
        predicted: int,
        expected: str
) -> None:
    mocked_prediction.return_value = predicted
    assert cryptocurrency_action(current) == expected
