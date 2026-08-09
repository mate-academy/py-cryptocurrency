from unittest import mock

import pytest

from app.main import cryptocurrency_action


# @pytest.fixture
# def mock_get_exchange_rate_prediction() -> float:
#     with mock.patch(
#         "app.main.get_exchange_rate_prediction"
#     ) as mock_exchange_rate_prediction:
#         yield mock_exchange_rate_prediction
#

@pytest.mark.parametrize(
    "current_rate,return_value, expected_result", [
        (100, 110, "Buy more cryptocurrency"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 0.94, "Sell all your cryptocurrency")
    ],
    ids=[
        "1",
        "2",
        "3",
        "4",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction: None,
        current_rate: int | float,
        return_value: int | float,
        expected_result: str,
) -> None:
    get_exchange_rate_prediction.return_value = return_value

    assert cryptocurrency_action(current_rate) == expected_result
