import pytest
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "mocked_exchange_rate, "
    "current_rate, "
    "expected_result",
    [
        (1.06, 1.0, "Buy more cryptocurrency"),
        (0.94, 1.0, "Sell all your cryptocurrency"),
        (0.95, 1.0, "Do nothing"),
        (1.05, 1.0, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        mocked_exchange_rate: float,
        current_rate: float,
        expected_result: str

) -> None:
    mocked_get_exchange_rate_prediction.return_value = mocked_exchange_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
