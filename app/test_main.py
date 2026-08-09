from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, expected_result",
    [
        (1.1, "Buy more cryptocurrency"),
        (0.9, "Sell all your cryptocurrency"),
        (1, "Do nothing"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing")
    ]
)
def test_cryptocurrency_action(prediction_rate: int,
                               expected_result: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction") as
          mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(1) == expected_result
