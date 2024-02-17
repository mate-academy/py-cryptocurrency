from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, expected_result",
    [
        pytest.param(
            4.3,
            5,
            "Buy more cryptocurrency",
            id="should recommend by more cryptocurrency "
               "if predicted rate > 1.05"
        ),
        pytest.param(
            5,
            5.1,
            "Do nothing",
            id="should recommend do nothing "
               "if predicted rate < 1.05 and > 0.95"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="should recommend do nothing "
               "if predicted rate == 0.95"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="should recommend do nothing "
               "if predicted rate == 1.05"
        ),
        pytest.param(
            5.8,
            5,
            "Sell all your cryptocurrency",
            id="should recommend sell all cryptocurrency "
               "if predicted rate < 0.95"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrecy_action(
        mocked_get_exchange_rate_prediction: MagicMock,
        current_rate: int | float,
        prediction: int | float,
        expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction

    result = cryptocurrency_action(current_rate)

    assert result == expected_result
