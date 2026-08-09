import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_prediction, expected",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing"),

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock.MagicMock,
        rate_prediction: int | float,
        expected: str
) -> None:
    mocked_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(100) == expected
