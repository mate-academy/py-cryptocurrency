from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency")
    ],
    ids=[
        "only 5 percent increase -> do nothing",
        "only 5 percent drop -> do nothing",
        "big increase -> buy more",
        "big drop -> sell all"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
    current_rate: int,
    prediction_rate: int,
    expected: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
    mocked_get_exchange_rate_prediction.assert_called_once_with(current_rate)
