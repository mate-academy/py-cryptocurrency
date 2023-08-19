import pytest

from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "rate_prediction, current_rate, expected_action",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (1, 1.06, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock,
        rate_prediction: int | float,
        current_rate: int | float,
        expected_action: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = rate_prediction

    assert cryptocurrency_action(current_rate) == expected_action
