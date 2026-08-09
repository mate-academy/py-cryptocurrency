from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_num, current_num, expected_result",
    [
        (105, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency"),
        (95, 100, "Do nothing"),
        (94, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_give_correct_result(
    mock_get_exchange_rate_prediction: mock.MagicMock,
    predicted_num: int | float,
    current_num: int | float,
    expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_num
    assert cryptocurrency_action(current_num) == expected_result
