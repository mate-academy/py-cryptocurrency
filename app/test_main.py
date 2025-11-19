from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 0, "Sell all your cryptocurrency"),
        (10, 10, "Do nothing"),
        (100, 95, "Do nothing"),

    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_rate_prediction: mock.MagicMock,
        current_rate: int,
        prediction_rate: int,
        expected_result: str
) -> None:
    mock_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result

    mock_exchange_rate_prediction.assert_called_once_with(current_rate)
