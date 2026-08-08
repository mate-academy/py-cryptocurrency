import pytest
from unittest.mock import patch

from _pytest.monkeypatch import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "percentage,expected_result",
    [
        (1.10, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (1.00, "Do nothing"),
        (0.95, "Do nothing"),
        (1.05, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: MonkeyPatch,
        percentage: float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = percentage * 100
    assert cryptocurrency_action(100) == expected_result
