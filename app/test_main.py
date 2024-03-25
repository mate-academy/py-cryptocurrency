from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,current_rate,expected_res",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (0.94, 1, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (1, 1, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        predicted_rate: float,
        current_rate: float | int,
        expected_res: bool,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_res
