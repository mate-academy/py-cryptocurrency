from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("current_rate", "expected_rate", "action"),
    [
        (20, 18, "Sell all your cryptocurrency"),
        (20, 22, "Buy more cryptocurrency"),
        (20, 19, "Do nothing"),
        (20, 20, "Do nothing"),
        (20, 21, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_predication: mock.MagicMock,
        current_rate: float,
        expected_rate: float,
        action: str
) -> None:
    mock_get_exchange_rate_predication.return_value = expected_rate
    assert cryptocurrency_action(current_rate) == action
