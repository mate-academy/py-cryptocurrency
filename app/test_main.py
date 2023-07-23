import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, expected_result", [
    (110.1, "Buy more cryptocurrency"),
    (92.6, "Sell all your cryptocurrency"),
    (55.3, "Do nothing")
], ids=["Buy more", "Sell all", "Do nothing"])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction,
                               current_rate: float,
                               expected_result: str) -> None:
    mock_get_exchange_rate_prediction.return_value = 55.3

    result = cryptocurrency_action(current_rate)
    assert result == expected_result
