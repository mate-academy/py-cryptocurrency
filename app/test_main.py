import pytest
from unittest.mock import patch
import app.main as ap


@pytest.mark.parametrize(
    "current_rate_template, exchange_rate_prediction, expected_result",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 103.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
    ]
)
def test_cryptocurrency_action(
    current_rate_template: float,
    exchange_rate_prediction: float,
    expected_result: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=exchange_rate_prediction):
        assert ap.cryptocurrency_action(
            current_rate_template) == expected_result
