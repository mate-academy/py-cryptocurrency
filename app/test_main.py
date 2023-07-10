from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_result,expected_result",
    [
        (106, "Buy more cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
        (99, "Do nothing"),
        (95, "Do nothing"),
        (105, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_values(
        mock_predict: callable,
        mock_result: int,
        expected_result: str,
) -> None:
    mock_predict.return_value = mock_result

    assert cryptocurrency_action(100) == expected_result
