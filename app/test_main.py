from unittest.mock import Mock, patch
import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "mocked_value, expected_result",
    [
        (1.1, "Buy more cryptocurrency"),
        (0.9, "Sell all your cryptocurrency"),
        (1.04, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: Mock,
        mocked_value: float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = mocked_value

    assert cryptocurrency_action(mocked_value) == expected_result
