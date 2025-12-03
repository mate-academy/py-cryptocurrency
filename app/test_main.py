from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action

current_exchange_rate = 100


@pytest.mark.parametrize(
    "predicted_value, expected_string",
    [
        pytest.param(106, "Buy more cryptocurrency"),
        pytest.param(94, "Sell all your cryptocurrency"),
        pytest.param(105, "Do nothing"),
        pytest.param(95, "Do nothing")
    ]

)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Mock,
        predicted_value: float | int,
        expected_string: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_value
    assert cryptocurrency_action(current_exchange_rate) == expected_string
