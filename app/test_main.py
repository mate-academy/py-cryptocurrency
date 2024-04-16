from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current_rate, expected", [
        (50, 1, "Buy more cryptocurrency"),
        (1, 50, "Sell all your cryptocurrency"),
        (50, 49, "Do nothing"),
    ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_main(mocked_exchange_rate_prediction: None,
              prediction: int,
              current_rate: int,
              expected: str
              ) -> None:
    mocked_exchange_rate_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected

