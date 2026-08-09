from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_prediction_value, current_rate, result",
    [
        (4.75, 5, "Do nothing"),
        (4.2, 4, "Do nothing"),
        (4, 4, "Do nothing"),
        (6, 4, "Buy more cryptocurrency"),
        (4, 8, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_can_access_google_page(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        rate_prediction_value: int | float,
        current_rate: int | float,
        result: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = rate_prediction_value
    assert cryptocurrency_action(current_rate=current_rate) == result
