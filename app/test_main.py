from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_prediction,expected_action",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (100, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock.MagicMock,
        rate_prediction: int | float,
        expected_action: str
) -> None:
    mocked_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(100) == expected_action
