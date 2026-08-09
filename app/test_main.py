from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate_prediction, expected",
    [
        (
            95,
            "Do nothing",
        ),
        (
            105,
            "Do nothing",
        ),
        (
            110,
            "Buy more cryptocurrency",
        ),
        (
            90,
            "Sell all your cryptocurrency",
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_correct_action(
        mocked_prediction: mock.MagicMock,
        exchange_rate_prediction: int,
        expected: str
) -> None:
    mocked_prediction.return_value = exchange_rate_prediction
    assert cryptocurrency_action(100) == expected
