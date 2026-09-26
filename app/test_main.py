from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("predicted_rate", "expected"),
    [
        pytest.param(106,
                     "Buy more cryptocurrency",
                     id="above_upper_boundary"),
        pytest.param(105, "Do nothing", id="at_upper_boundary"),
        pytest.param(100, "Do nothing", id="unchanged"),
        pytest.param(95, "Do nothing",
                     id="at_lower_boundary"),
        pytest.param(94, "Sell all your cryptocurrency",
                     id="below_lower_boundary"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_returns_expected_action(
    mock_rate_prediction: mock.Mock,
    predicted_rate: int,
    expected: str,
) -> None:
    mock_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate=100) == expected
