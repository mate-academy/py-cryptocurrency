import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rat, prediction_rate, expected",
    [
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 1.0501, "Buy more cryptocurrency"),
        (1, 0.9499, "Sell all your cryptocurrency"),
    ]
)
def test_process_data(current_rat: int | float,
                      prediction_rate: int | float,
                      expected: str
                      ) -> None:
    with (patch("app.main.get_exchange_rate_prediction") as
          mocked_get_exchange_rate):
        mocked_get_exchange_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rat) == expected
