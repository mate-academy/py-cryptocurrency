from unittest import mock

import pytest
import app.main


@pytest.mark.parametrize(
    "current_rate , prediction_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
    ])
def test_exchange_rate(
        current_rate: int,
        prediction_rate: int,
        expected: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = prediction_rate
        result = app.main.cryptocurrency_action(current_rate)
        assert result == expected
