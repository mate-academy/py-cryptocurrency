from unittest import mock

import app.main
import pytest


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 1.02, "Do nothing"),
        (1.0, 0.98, "Do nothing"),
        (1.0, 0.95, "Do nothing"),
        (1.0, 0.94, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_main(get_exchange_rate_prediction: mock.MagicMock,
              current_rate: float,
              predicted_rate: float,
              expected: str) -> None:
    get_exchange_rate_prediction.return_value = predicted_rate

    result = app.main.cryptocurrency_action(current_rate)
    assert result == expected
